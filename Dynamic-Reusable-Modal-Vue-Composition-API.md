# Dynamic Reusable Modal Component (Vue 3 + Composition API)

This document captures the design, implementation, and explanation of a
**dynamic reusable modal component** built using **Vue 3** and the
**Composition API**.

------------------------------------------------------------------------

## 1. Initial Requirements

The goal was to create a reusable modal component with the following
features:

1.  The modal may or may not have a title
2.  It has 2 default buttons:
    -   Cancel
    -   OK
3.  Default buttons:
    -   Can be hidden
    -   Can have their labels overridden
4.  Developers can:
    -   Add additional custom buttons
    -   Fully replace the footer if needed
5.  Uses Vue 3 Composition API
6.  Should work cleanly anywhere in the app

------------------------------------------------------------------------

## 2. BaseModal.vue (Initial Implementation)

### Features

-   Optional title
-   Default Cancel / OK buttons
-   Footer slot for customization
-   Uses v-model for open/close
-   Uses Teleport to render outside parent DOM

``` vue
<template>
  <Teleport to="body">
    <div v-if="modelValue" class="modal-overlay" @click.self="emitClose">
      <div class="modal-container">
        <header v-if="title || $slots.header">
          <slot name="header">
            <h3>{{ title }}</h3>
          </slot>
        </header>
        <section>
          <slot />
        </section>
        <footer>
          <slot name="footer">
            <button v-if="showCancel">Cancel</button>
            <button v-if="showOk">OK</button>
          </slot>
        </footer>
      </div>
    </div>
  </Teleport>
</template>
```

------------------------------------------------------------------------

## 3. Enhancement: Overridable Button Labels

``` js
okText: {
  type: String,
  default: 'OK'
},
cancelText: {
  type: String,
  default: 'Cancel'
}
```

------------------------------------------------------------------------

## 4. Usage Examples

### Override Button Text

``` vue
<BaseModal
  v-model="isOpen"
  title="Delete Item"
  okText="Delete"
  cancelText="Keep"
>
  Are you sure?
</BaseModal>
```

------------------------------------------------------------------------

## 5. Explanation: Vue Teleport

Teleport allows rendering DOM content outside the component hierarchy,
commonly used for modals and overlays.

------------------------------------------------------------------------

## 6. Summary

-   Fully reusable modal
-   Configurable defaults
-   Slot-based customization
-   Teleport ensures proper overlay behavior
