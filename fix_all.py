import re
import os

# 1. seed.js
with open("backend/src/db/seed.js", "r") as f:
    seed = f.read()
seed = seed.replace("VALUES (?, ?, ?, ?, ?, ?, ?)", "VALUES (?, ?, ?, ?, ?, ?)")
seed = seed.replace(
    "Buffer.from('8J+aqCBJTlRFUk5BTCBPTkxZIPCfmqggUHJvZHVjdGlvbiBtb2xkcyBmb3IgQnVnID8/Py4gRmFjdG9yeSBjb29yZGluYXRlczogNDcuMTIzNMKwTiwgMTcyLjU2NzjCsFcuIEFjY2VzcyBDb2RlOiBGTEFHe2lkb3JfbGVha2VkX2ZhY3RvcnlfbW9sZHN9LiBETyBOT1QgU0hBUkUgT1VUU0lERSBERVNJR04gVEVBTS4=', 'base64').toString('utf-8')",
    "'🚨 INTERNAL ONLY 🚨 Production molds for Bug ???. Factory coordinates: 47.1234°N, 172.5678°W. Access Code: ' + generateFlag('idor_orders') + '. DO NOT SHARE OUTSIDE DESIGN TEAM.'"
)
with open("backend/src/db/seed.js", "w") as f:
    f.write(seed)

# 2. reviews.js
with open("backend/src/routes/reviews.js", "r") as f:
    reviews = f.read()
reviews = "const { generateFlag } = require('../utils/flags');\n" + reviews
reviews = re.sub(r"flag = db\.prepare\('SELECT flag_value FROM flags WHERE challenge_key = \?'\)\.get\('stored_xss'\);", "flag = generateFlag('stored_xss');", reviews)
reviews = reviews.replace("flag ? flag.flag_value : undefined", "flag ? flag : undefined")
with open("backend/src/routes/reviews.js", "w") as f:
    f.write(reviews)

# 3. orders.js
with open("backend/src/routes/orders.js", "r") as f:
    orders = f.read()
orders = "const { generateFlag } = require('../utils/flags');\n" + orders
orders = re.sub(r"flag = db\.prepare\('SELECT flag_value FROM flags WHERE challenge_key = \?'\)\.get\('idor_orders'\);", "flag = generateFlag('idor_orders');", orders)
orders = orders.replace("flag ? flag.flag_value : undefined", "flag ? flag : undefined")
with open("backend/src/routes/orders.js", "w") as f:
    f.write(orders)

# 4. payment.js
with open("backend/src/routes/payment.js", "r") as f:
    payment = f.read()
payment = re.sub(r"flag = db\.prepare\('SELECT flag_value FROM flags WHERE challenge_key = \?'\)\.get\('payment_bypass'\);", "flag = generateFlag('payment_bypass');", payment)
# We need to make sure 'flag' is used correctly. 
payment = payment.replace("flag: flag_value", "flag: flag")
# I'll just check payment.js closely. Wait, it used to be flag ? flag.flag_value : undefined. I changed it to flag_value. Let's fix it.
payment = payment.replace("flag = generateFlag('payment_bypass');", "const flag_value = generateFlag('payment_bypass');\n      flag = flag_value;") # Keep it simple
with open("backend/src/routes/payment.js", "w") as f:
    f.write(payment)

# 5. App.jsx (SOC)
with open("frontend-soc/src/App.jsx", "r") as f:
    app_jsx = f.read()
# Replace Reset CTF Progress button with PanicButton
button_code = """<button
              onClick={resetProgress}
              style={{
                marginTop: 'auto',
                padding: '12px',
                backgroundColor: 'transparent',
                border: '1px solid var(--border)',
                color: 'var(--text-muted)',
                borderRadius: '6px',
                fontSize: '11px',
                cursor: 'pointer',
                textAlign: 'center'
              }}
            >
              Reset CTF Progress
            </button>"""
import_panic = "import PanicButton from './components/PanicButton';"

if import_panic not in app_jsx:
    app_jsx = app_jsx.replace("import StatsBar", "import PanicButton from './components/PanicButton';\nimport StatsBar")
app_jsx = app_jsx.replace(button_code, "<PanicButton onResetCtf={resetProgress} />")
with open("frontend-soc/src/App.jsx", "w") as f:
    f.write(app_jsx)

# 6. Remove fix_backup.py
try:
    os.remove("fix_backup.py")
except:
    pass

