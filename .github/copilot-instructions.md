# Kniha Jazd - AI Coding Guidelines

## Project Overview
Single-file HTML application for Slovak vehicle activity logging. No build process required - open `kniha_jazd.html` directly in browser.

## Architecture Patterns
- **Single-file design**: HTML + CSS + JS in one file
- **State management**: Global variables (`current`, `entries`) with localStorage persistence
- **Activity system**: Predefined activities in `ACTS` array with id/label/color/icon properties
- **Functional rendering**: `render()` calls update all UI components

## Code Conventions
- **Activity IDs**: Use kebab-case (e.g., `'ina-praca'`, `'prestávka'`)
- **Color theming**: CSS custom properties (`--c`) for activity colors
- **Time formatting**: Slovak locale (`sk-SK`) for timestamps
- **Duration format**: `HH:MM:SS` or `MM:SS` depending on hours
- **State persistence**: JSON serialization of Date objects as timestamps

## Key Functions
- `trigger(act)`: Main state transition handler
- `render()`: Updates all UI components
- `saveState()`/`loadState()`: localStorage persistence
- Export functions: `exportCSV()`, `exportICS()`

## UI Patterns
- **Status panel**: Shows current activity with color-coded border
- **Activity buttons**: Grid layout with icons, color-coded by activity
- **Log table**: Chronological entries with badges and durations
- **Summary panel**: Aggregated time totals per activity

## Export Formats
- **CSV**: Excel-compatible with BOM for Slovak characters
- **ICS**: Google Calendar events with activity details
- **Print**: CSS media queries hide interactive elements

## Development Workflow
1. Edit `kniha_jazd.html` directly
2. Test by opening in browser
3. Data persists in localStorage across sessions
4. Export functions generate downloadable files

## Adding New Activities
1. Add to `ACTS` array with id/label/color/icon
2. Button automatically created in `buildButtons()`
3. Export functions handle new activities automatically</content>
<parameter name="filePath">c:\Users\peter\Nový priečinok\Claude_code\.github\copilot-instructions.md