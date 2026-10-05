import re

with open("backend/src/routes/system.js", "r") as f:
    content = f.read()

route = """
// VULN: Information Disclosure (Backup file left on server)
router.get('/backup.bak', (req, res) => {
  const db = req.app.get('db');
  const flag = db.prepare('SELECT flag_value FROM flags WHERE challenge_key = ?').get('info_disclosure');
  const fileContent = `DB_CONNECTION=sqlite\nDB_DATABASE=bugdrop.db\nADMIN_EMAIL=admin@bugdrop.local\nFLAG=${flag ? flag.flag_value : 'FLAG_NOT_FOUND'}\nDEBUG=true\n`;
  
  res.setHeader('Content-disposition', 'attachment; filename=backup.bak');
  res.setHeader('Content-type', 'text/plain');
  res.send(fileContent);
});

"""

if "backup.bak" not in content:
    content += route
    with open("backend/src/routes/system.js", "w") as f:
        f.write(content)
