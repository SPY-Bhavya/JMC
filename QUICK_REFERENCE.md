# JMC Theme - Quick Reference Guide

## 🎨 JMC Color Palette

```css
/* Primary Colors */
--jmc-green: #05231c;        /* Dark green - Headers, Text, Navigation */
--jmc-cream: #f9f5f0;        /* Cream - Backgrounds */
--jmc-gold: #d4af37;         /* Gold - Accents, Buttons, CTAs */
--jmc-gold-light: #e5c567;   /* Light Gold - Hover states */
```

### Usage Examples

```html
<!-- Using CSS Variables -->
<div style="background-color: var(--jmc-cream);">
  <h1 style="color: var(--jmc-green);">JMC Jewellers</h1>
  <button style="background-color: var(--jmc-gold);">Shop Now</button>
</div>

<!-- Using Tailwind Classes -->
<div class="bg-jmc-cream">
  <h1 class="text-jmc-green">JMC Jewellers</h1>
  <button class="bg-jmc-gold">Shop Now</button>
</div>
```

## 🔤 Font Families

```css
/* Headings (Serif) */
font-family: "Playfair Display", serif;

/* Body Text (Sans-serif) */
font-family: "Lato", sans-serif;
```

### Font Weights Available

**Playfair Display:**
- 400 (Regular)
- 600 (Semi-Bold)
- 400 Italic

**Lato:**
- 300 (Light)
- 400 (Regular)
- 700 (Bold)

## 📁 Files Overview

| File | Size | Description |
|------|------|-------------|
| **Manish_Malhotra_Original.html** | 6.5MB | Original unmodified file |
| **Manish_Malhotra_Formatted.html** | 6.6MB | **✅ USE THIS - Formatted + JMC Theme** |
| **JMC_Themed_Final.html** | 6.6MB | Same as formatted (backup) |
| **JMC.html** | 80KB | Alternative clean template |
| **index.html** | 80KB | Current working file |

## 🎯 What to Use

### For Reference Design (with JMC colors):
👉 **Use: `Manish_Malhotra_Formatted.html`**
- Has JMC colors applied
- Proper indentation
- Ready to extract sections from

### For Clean Development:
👉 **Use: `JMC.html` or `index.html`**
- Lightweight (80KB)
- Clean Tailwind CSS
- Easy to modify

## ✅ Theme Applied Features

- [x] 199 color replacements
- [x] JMC Green (#05231c) for dark/primary
- [x] JMC Cream (#f9f5f0) for backgrounds
- [x] JMC Gold (#d4af37) for accents
- [x] Playfair Display font
- [x] Lato font
- [x] Tailwind config
- [x] CSS variables
- [x] Proper indentation

## 🛠️ Utility Scripts

| Script | Purpose |
|--------|---------|
| `format_html.py` | Format/indent HTML files |
| `analyze_colors.py` | Extract all colors from HTML |
| `apply_jmc_colors.py` | Apply JMC color scheme |
| `update_fonts.py` | Update fonts to JMC theme |
| `verify_theme.py` | Verify theme is applied correctly |
| `analyze_structure.py` | Analyze HTML structure |

### How to Use Scripts

```bash
# Format an HTML file
python format_html.py

# Analyze colors
python analyze_colors.py

# Apply JMC theme
python apply_jmc_colors.py

# Verify theme
python verify_theme.py
```

## 📊 Statistics

- **Total Color Replacements**: 199
- **JMC Brand Colors Used**: 106 times
- **Other Colors Remaining**: 58 occurrences (functional)
- **Font References**: Playfair Display (1), Lato (3)
- **File Size**: 6.6MB (formatted with theme)

## 🎨 Color Breakdown

| Color | Usage Count | Purpose |
|-------|-------------|---------|
| JMC Green | 50 | Primary text, headers |
| JMC Cream | 52 | Backgrounds |
| JMC Gold | 3 | Accent elements |
| JMC Gold Light | 1 | Light accents |
| White | 28 | Text on dark backgrounds |
| Other | 30 | Various UI elements |

## 📖 Documentation

- **CONVERSION_PLAN.md** - Full conversion roadmap
- **THEME_UPDATE_SUMMARY.md** - Detailed theme application report
- **structure_analysis.txt** - HTML structure breakdown
- **color_analysis.txt** - Original color analysis
- **JMC_Themed_Final_verification_report.txt** - Theme verification

## 🚀 Next Steps

1. Review the themed file in browser
2. Start content conversion (text, images)
3. Update navigation menus
4. Replace product categories
5. Add JMC-specific sections

---

**Quick Start**: Open `Manish_Malhotra_Formatted.html` to see the JMC themed design!
