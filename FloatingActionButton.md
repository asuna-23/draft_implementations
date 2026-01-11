# FloatingActionButton – Dynamic & Reusable (Vue 3 + Composition API)

The **FloatingActionButton (FAB)** is a reusable, dynamic Vue 3 component that allows you to create a floating action button with optional expandable actions. It is fully customizable and framework-agnostic.

---

## Table of Contents

1. Overview
2. Key Features
3. How This Differs From Other Frameworks
4. Requirements
5. Installation
6. Props API
7. Slots
8. Usage Examples
9. Component Code
10. Advantages
11. Best Practices
12. Accessibility Considerations
13. FAQ

---

## 1. Overview

A Floating Action Button (FAB) is a circular button that floats above the UI and represents a primary action. This component is dynamic, allowing multiple positions, sizes, icons, and optional expandable actions.

---

## 2. Key Features

* Dynamic positions: `bottom-right`, `bottom-left`, `top-right`, `top-left`
* Multiple sizes: `small`, `medium`, `large`
* Custom icons (Font Awesome, Material, SVG)
* Expandable sub-actions with animation
* Slot support for custom icons and actions
* Fully framework-agnostic
* Toggle visibility dynamically
* Accessible with ARIA attributes

---

## 3. How This Differs From Other Frameworks

| Framework    | Limitation                                 | Dynamic FAB Advantage                                        |
| ------------ | ------------------------------------------ | ------------------------------------------------------------ |
| Bootstrap    | Only regular buttons, no floating behavior | Fully floating, configurable, expandable actions, slot-based |
| Vuetify      | Material-only style, fixed behavior        | Fully dynamic, reusable, framework-agnostic                  |
| Quasar       | Mobile-centric FABs                        | Desktop & mobile ready, flexible slots                       |
| Element Plus | No FAB                                     | Fully reusable, configurable, slot-based actions             |

---

## 4. Requirements

* Vue 3
* Composition API
* JavaScript (no TypeScript required)

---

## 5. Installation

Add the component to your project:

```
src/components/FloatingActionButton/
 ├── FloatingActionButton.vue
 └── index.js
```

Register it globally or locally.

---

## 6. Props API

| Prop          | Type    | Default                    | Description                                            |
| ------------- | ------- | -------------------------- | ------------------------------------------------------ |
| `icon`        | String  | `'plus'`                   | Main button icon                                       |
| `position`    | String  | `'bottom-right'`           | FAB position on screen                                 |
| `size`        | String  | `'medium'`                 | Button size: small, medium, large                      |
| `color`       | String  | `'#3498db'`                | Button color                                           |
| `expandable`  | Boolean | `false`                    | Whether it shows expandable actions                    |
| `visible`     | Boolean | `true`                     | Whether FAB is visible                                 |
| `ariaLabel`   | String  | `'Floating Action Button'` | ARIA label for accessibility                           |
| `actionItems` | Array   | `[]`                       | Array of sub-action objects `{ icon, label, onClick }` |

---

## 7. Slots

* ``: Replace main FAB icon
* ``: Replace expandable action buttons with custom template

---

## 8. Usage Examples

### Single FAB

```vue
<FloatingActionButton icon="plus" @click="openForm" />
```

### Expandable FAB with Actions

```vue
<FloatingActionButton
  expandable
  :action-items="[
    { icon: 'edit', label: 'Edit', onClick: editItem },
    { icon: 'trash', label: 'Delete', onClick: deleteItem },
    { icon: 'file', label: 'New File', onClick: newFile }
  ]"
/>
```

### Positioned FAB

```vue
<FloatingActionButton position="bottom-left" icon="edit" />
```

---

## 9. Component Code

*(Full Vue 3 + Composition API code is included above)*

---

## 10. Advantages

* Single reusable FAB component
* Supports single or multiple actions
* Fully customizable with props and slots
* Framework-agnostic, works with any UI style
* Expandable actions with animation
* Accessible

---

## 11. Best Practices

* Use primary actions for main FAB
* Expandable FAB for secondary tasks
* Avoid too many sub-actions to reduce complexity
* Keep consistent positioning across app

---

## 12. Accessibility Considerations

* Add `aria-label` for main button
* Use ARIA `aria-expanded` for expandable actions
* Ensure keyboard navigation works

---

## 13. FAQ

**Q: Can I use this with Bootstrap?** A: Yes, it is fully framework-agnostic.

**Q: Can it have multiple actions?** A: Yes, using the `expandable` prop and `actionItems` array.

**Q: Can I customize icons?** A: Yes, via the `icon` prop or slot.

---

## Conclusion

The **FloatingActionButton** is a dynamic, reusable, and customizable Vue 3 component that can handle both single and multiple actions. It is fully framework-agnostic and ready for production applications.
