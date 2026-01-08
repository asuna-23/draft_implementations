# Confirmable Action Wrapper (Vue 3)

## Overview

A reusable wrapper component that asks for confirmation before executing
an action. Internally, it can reuse a modal component.

## Use Case

-   Delete actions
-   Destructive operations
-   Sensitive updates

## Implementation

### ConfirmAction.vue

``` vue
<template>
  <span @click="open = true">
    <slot />
  </span>

  <BaseModal
    v-model="open"
    :title="title"
    @ok="confirm"
  >
    {{ message }}
  </BaseModal>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  title: { type: String, default: 'Confirm Action' },
  message: { type: String, required: true }
})

const emit = defineEmits(['confirm'])
const open = ref(false)

const confirm = () => emit('confirm')
</script>
```

## Usage

``` vue
<ConfirmAction
  message="Delete this item?"
  @confirm="deleteItem"
>
  <button class="danger">Delete</button>
</ConfirmAction>
```
