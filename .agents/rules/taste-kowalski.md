---
name: frontend-taste-kowalski
description: Impeccable design rules, Emil Kowalski aesthetics, and general good taste for UI/UX.
trigger: always_on
---
# Taste & Impeccable Design (Emil Kowalski Standards)

Cuando generes código frontend o interfaces de usuario, DEBES cumplir los siguientes estándares para garantizar una calidad visual premium (evitando el aspecto genérico de IA):

## 1. Tipografía y Espaciado (Impeccable)
- Usa fuentes premium como **Geist**, **Inter** o **SF Pro**.
- Implementa un sistema de espaciado estricto basado en múltiplos de 4 (4px, 8px, 16px, 24px, 32px...).
- El espacio en blanco (whitespace) es fundamental. Los elementos deben "respirar".
- No uses negro puro (#000) para el texto. Usa grises muy oscuros (ej. `zinc-900`) y grises sutiles (`zinc-500`) para subtítulos.

## 2. Animaciones y Físicas (Estilo Emil Kowalski)
- NUNCA uses transiciones lineales simples (CSS `ease` o `linear`).
- Usa físicas de rebote (Spring Physics) para animaciones, similares a las de Framer Motion (ej. stiffness: 400, damping: 30).
- **Micro-interacciones:** Los botones deben reaccionar al click reduciéndose muy sutilmente (`scale: 0.97`) y tener transiciones suaves en hover.
- Elementos que aparecen en pantalla deben tener un efecto sutil de `fade-in-up`.

## 3. Criterio Visual (Taste Skill)
- **Sombras:** Prohibidas las sombras duras. Usa sombras difusas, multicapa y muy suaves con opacidades del 2% al 5%.
- **Bordes:** Define la separación entre elementos mediante bordes muy sutiles (ej. `border-zinc-200` o `border-white/10` en modo oscuro) en lugar de usar fondos de colores pesados.
- **Materiales:** Usa efectos de cristal (Glassmorphism con `backdrop-blur`) en menús de navegación fijos.

## 4. Stack Técnico Preferido
- Usa Tailwind CSS.
- Si usas React, apóyate en Framer Motion y componentes accesibles como Radix UI o Lucide Icons.
