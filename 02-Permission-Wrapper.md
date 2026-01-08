# Permission Wrapper (Vue 3)

## Overview

A wrapper component that conditionally renders content based on user
permissions.

## Use Case

-   Role-based UI
-   Feature gating
-   Admin controls

## Implementation

### Can.vue

``` vue
<template>
  <slot v-if="allowed" />
</template>

<script setup>
import { inject, computed } from 'vue'

const props = defineProps({
  permission: { type: String, required: true }
})

const permissions = inject('permissions', [])

const allowed = computed(() =>
  permissions.includes(props.permission)
)
</script>
```

## Usage

``` vue
<Can permission="user.delete">
  <button>Delete User</button>
</Can>
```

## Notes

Permissions are expected to be provided globally using `provide()`.
