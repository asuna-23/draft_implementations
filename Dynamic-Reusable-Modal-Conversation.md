# Dynamic Reusable Modal (Vue 3 + Composition API)

## User Request

**I want to create a dynamic reusable modal using Vue.js and the
Composition API with the following requirements:**

1.  The modal can have or not have a title.
2.  It has 2 default buttons --- **Cancel** and **OK**.
    -   These default buttons can be hidden if the developer wants.
    -   Aside from the default buttons, the developer can add more
        buttons.

------------------------------------------------------------------------

## Response: Reusable Modal Design

To achieve this, we create a reusable `BaseModal` component that uses:

-   **Props** for configuration
-   **Slots** for customization
-   **v-model** for open/close control
-   **Teleport** to ensure the modal renders properly as an overlay

### Key Design Decisions

-   The title is optional and only rendered when provided.
-   Default buttons (Cancel / OK) are shown by default.
-   Button visibility can be controlled via props.
-   A footer slot allows developers to add or replace buttons entirely.

------------------------------------------------------------------------

## Enhancement Request

**The OK and Cancel button titles can be overridden as well.**

------------------------------------------------------------------------

## Response: Overridable Button Titles

To support customizable button text, we introduce two additional props:

-   `okText` --- controls the OK button label
-   `cancelText` --- controls the Cancel button label

### Default Values

-   `okText`: `"OK"`
-   `cancelText`: `"Cancel"`

This allows developers to quickly change button labels without rewriting
the footer.

------------------------------------------------------------------------

## Example API

### Props Summary

-   `modelValue` (Boolean) --- controls modal visibility
-   `title` (String) --- optional modal title
-   `showOk` (Boolean) --- show/hide OK button
-   `showCancel` (Boolean) --- show/hide Cancel button
-   `okText` (String) --- OK button label
-   `cancelText` (String) --- Cancel button label

------------------------------------------------------------------------

## Example Usage

``` vue
<BaseModal
  v-model="isOpen"
  title="Delete Item"
  okText="Delete"
  cancelText="Keep"
>
  Are you sure you want to delete this item?
</BaseModal>
```

------------------------------------------------------------------------

## Summary

-   The modal is fully reusable and configurable.
-   Defaults allow quick usage with minimal setup.
-   Slots provide advanced customization.
-   Button labels are easily overridden via props.
-   This approach follows best practices used by modern Vue UI
    libraries.
