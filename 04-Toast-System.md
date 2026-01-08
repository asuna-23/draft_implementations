# Toast Notification System (Vue 3)

## Overview

A lightweight global toast system using a composable and Teleport.

## Use Case

-   Success messages
-   Error notifications
-   System feedback

## Implementation

### useToast.js

``` js
import { reactive } from 'vue'

const state = reactive({
  toasts: []
})

export function useToast() {
  const push = (type, message) => {
    state.toasts.push({ id: Date.now(), type, message })
    setTimeout(() => state.toasts.shift(), 3000)
  }

  return {
    success: msg => push('success', msg),
    error: msg => push('error', msg),
    state
  }
}
```

### ToastContainer.vue

``` vue
<template>
  <Teleport to="body">
    <div class="toast-container">
      <div
        v-for="toast in state.toasts"
        :key="toast.id"
        class="toast"
      >
        {{ toast.message }}
      </div>
    </div>
  </Teleport>
</template>

<script setup>
import { useToast } from './useToast'
const { state } = useToast()
</script>
```

## Usage

``` js
const toast = useToast()
toast.success('Saved successfully')
```
