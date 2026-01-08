# Inline Editable Field (Vue 3)

## Overview

A component that allows inline editing of text values with save-on-blur
or enter behavior.

## Use Case

-   Editable profile fields
-   Table cell editing
-   Quick updates

## Implementation

### InlineEdit.vue

``` vue
<template>
  <span v-if="!editing" @click="startEdit">
    {{ modelValue }}
  </span>

  <input
    v-else
    ref="input"
    v-model="value"
    @blur="save"
    @keyup.enter="save"
  />
</template>

<script setup>
import { ref, watch, nextTick } from 'vue'

const props = defineProps({
  modelValue: String
})

const emit = defineEmits(['update:modelValue', 'save'])

const editing = ref(false)
const value = ref(props.modelValue)
const input = ref(null)

watch(() => props.modelValue, v => value.value = v)

const startEdit = async () => {
  editing.value = true
  await nextTick()
  input.value.focus()
}

const save = () => {
  editing.value = false
  emit('update:modelValue', value.value)
  emit('save', value.value)
}
</script>
```

## Usage

``` vue
<InlineEdit v-model="username" @save="updateName" />
```
