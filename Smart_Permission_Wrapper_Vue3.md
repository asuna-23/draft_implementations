# Smart Permission Wrapper (Vue 3 + Composition API – JavaScript)

A **Smart Permission Wrapper** is a reusable, logic-first Vue component that controls **visibility, interactivity, and fallback UI** based on user roles, permissions, or feature flags.

This documentation is written for **Vue 3 using the Composition API with plain JavaScript (NOT TypeScript)**.

---

## Table of Contents
1. Overview  
2. Key Features  
3. How This Differs from Bootstrap  
4. Requirements  
5. Installation  
6. Basic Usage  
7. Component API (Props)  
8. Slots  
9. Permission Modes  
10. Full Component Code  
11. Integration Examples  
12. Accessibility Considerations  
13. Best Practices  
14. Suggested Folder Structure  
15. Extending the Component  
16. Limitations & Security Notes  
17. FAQ  

---

## 1. Overview

In many applications, permission checks are scattered across templates using `v-if`, `v-show`, or `:disabled`. This leads to:

- Repetitive logic  
- Hard-to-maintain templates  
- Inconsistent access control  

The **Smart Permission Wrapper** centralizes this logic into a single reusable component.

You wrap any UI element once, declare who is allowed, and the component decides what happens.

---

## 2. Key Features

- Vue 3 + Composition API (JavaScript)
- Role- or permission-based access control
- Multiple denial behaviors: `hide`, `disable`, `replace`
- Slot-based rendering
- UI-library agnostic (Bootstrap, Tailwind, custom CSS)
- Clean, declarative API
- Easy integration with Pinia or API data

---

## 3. How This Differs from Bootstrap

Bootstrap is a **styling framework**, not a logic framework.

| Bootstrap | Smart Permission Wrapper |
|---------|--------------------------|
| CSS-first | Logic-first |
| Visual utilities | Business-rule enforcement |
| `d-none`, `disabled` | Permission-aware rendering |
| No auth awareness | Integrates with auth state |

**Bootstrap answers:** *How does it look?*  
**Smart Permission Wrapper answers:** *Who is allowed to use it?*

This component can be used **with Bootstrap**, but Bootstrap alone cannot replace it.

---

## 4. Requirements

- Vue 3
- Composition API
- JavaScript (TypeScript not required)

Optional but recommended:
- Pinia
- Backend-authenticated permissions

---

## 5. Installation

```
src/components/permission/
 ├── PermissionGuard.vue
 └── index.js
```

---

## 6. Basic Usage

```vue
<PermissionGuard :allow="['admin', 'editor']">
  <button class="btn btn-primary">Edit Post</button>
</PermissionGuard>
```

---

## 10. Full Component Code

```vue
<script setup>
import { computed } from 'vue'

const props = defineProps({
  allow: {
    type: Array,
    required: true
  },
  mode: {
    type: String,
    default: 'hide'
  }
})

const userRoles = ['editor']

const isAllowed = computed(() => {
  return props.allow.some(role => userRoles.includes(role))
})
</script>
```
