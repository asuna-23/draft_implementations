# LoadingSpinner – Dynamic & Reusable (Vue 3 + Composition API)

The **LoadingSpinner** is a reusable, dynamic Vue 3 component that allows you to show different types of loading animations. Unlike typical loading spinners, this component is **not limited to circular spinners**; it supports multiple types and can be fully customized.

It is ideal for any Vue 3 project, giving developers flexibility while keeping the API simple and consistent.

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

Many frameworks offer only one type of loader or require multiple components for different loader types. **LoadingSpinner** centralizes multiple loader types into a single reusable component, simplifying integration and customization.

---

## 2. Key Features

- Multiple loader types: `circle`, `dots`, `bars`, `linear`
- Configurable props: `type`, `size`, `color`, `speed`, `fullscreen`, `text`
- Slot support for custom loaders
- Fullscreen overlay option
- Composition API compatible
- Works with any UI framework (Bootstrap, Tailwind, custom CSS)

---

## 3. How This Differs From Other Frameworks

| Framework | Limitation | LoadingSpinner Advantage |
|-----------|------------|------------------------|
| Bootstrap | Circular spinner only | Supports multiple loader types (`circle`, `dots`, `bars`, `linear`) and dynamic customization |
| Vuetify | Framework-specific styling | UI-library agnostic, can be used with any CSS framework |
| Element Plus | Mostly single spinner type, separate components for different loaders | Single reusable component for all types |
| Quasar | Requires global configuration for custom loader | Flexible props and slot for custom loader templates |

**Key difference:** LoadingSpinner is **dynamic, reusable, and framework-agnostic**, giving developers full control over style, size, type, and overlay behavior.

---

## 4. Requirements

- Vue 3
- Composition API
- JavaScript (no TypeScript required)

Optional:
- Pinia for global loader state
- Backend or API integration for async loading

---

## 5. Installation

Add the component to your project:

```
src/components/LoadingSpinner/
 ├── LoadingSpinner.vue
 └── index.js
```

Register it globally or locally.

---

## 6. Props API

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `type` | String | `'circle'` | Loader type: `circle`, `dots`, `bars`, `linear` |
| `size` | Number/String | `'medium'` | Size of the loader |
| `color` | String | `'#3498db'` | Loader color |
| `speed` | Number | `1` | Animation speed multiplier |
| `fullscreen` | Boolean | `false` | Overlay entire screen |
| `text` | String | `''` | Optional text below loader |
| `visible` | Boolean | `false` | Whether loader is shown |

---

## 7. Slots

- **Default slot** – Replace the loader with a fully custom template.

```vue
<LoadingSpinner v-if="loading">
  <img src="custom-loader.gif" />
</LoadingSpinner>
```

---

## 8. Usage Examples

### Circular Loader
```vue
<LoadingSpinner type="circle" :size="60" color="#ff3d00" :visible="loading" />
```

### Dots Loader
```vue
<LoadingSpinner type="dots" :size="40" color="#2ecc71" :visible="loading" />
```

### Linear / Progress Bar
```vue
<LoadingSpinner type="linear" :size="6" color="#3498db" :visible="loading" />
```

### Fullscreen Loader with Text
```vue
<LoadingSpinner type="circle" fullscreen text="Loading data..." :visible="loading" />
```

---

## 9. Component Code

```vue
<template>
  <div v-if="visible" :class="['spinner-overlay', { fullscreen }]">
    <div v-if="type === 'circle'" :style="{ width: size+'px', height: size+'px', borderColor: color }" class="spinner-circle"></div>
    <div v-else-if="type === 'dots'" class="spinner-dots">
      <span v-for="i in 3" :key="i" :style="{ backgroundColor: color, animationDuration: speed+'s' }"></span>
    </div>
    <div v-else-if="type === 'bars'" class="spinner-bars">
      <span v-for="i in 5" :key="i" :style="{ backgroundColor: color, animationDuration: speed+'s' }"></span>
    </div>
    <div v-else-if="type === 'linear'" class="spinner-linear" :style="{ height: size+'px', backgroundColor: color, animationDuration: speed+'s' }"></div>
    <div v-if="text" class="spinner-text">{{ text }}</div>
    <slot />
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  type: { type: String, default: 'circle' },
  size: { type: [Number, String], default: 'medium' },
  color: { type: String, default: '#3498db' },
  speed: { type: Number, default: 1 },
  fullscreen: { type: Boolean, default: false },
  text: { type: String, default: '' },
  visible: { type: Boolean, default: false }
})
</script>

<style scoped>
.spinner-overlay {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.spinner-overlay.fullscreen {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255,255,255,0.6);
  z-index: 9999;
}
.spinner-circle {
  border: 6px solid #ccc;
  border-top-color: inherit;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
/* Additional styles for dots, bars, linear would be added here */
</style>
```

---

## 10. Advantages

- Single reusable loader for multiple types
- Dynamic and configurable without duplicating components
- Can overlay content or be inline
- Fully styleable
- Composition API-friendly

---

## 11. Best Practices

- Use fullscreen overlay for blocking actions
- Inline loaders for section-specific loading
- Keep loader consistent across app for UX
- Use slot for highly custom loaders if needed

---

## 12. Accessibility Considerations

- Add `aria-busy="true"` when content is loading
- Ensure text or label is present for screen readers
- Avoid flashing loaders for very short actions

---

## 13. FAQ

**Q: Can I use this with Bootstrap?**  
A: Yes, it is fully framework-agnostic.

**Q: Is it only circular spinner?**  
A: No, supports circle, dots, bars, and linear.

**Q: Can I customize the loader fully?**  
A: Yes, via props and default slot for custom templates.

---

## Conclusion

**LoadingSpinner** provides a **dynamic, flexible, and reusable loader** for Vue 3 applications, giving developers multiple loader types, customization options, and framework independence.

It is a professional and portfolio-ready component for dashboards, SaaS apps, and any Vue 3 project.
