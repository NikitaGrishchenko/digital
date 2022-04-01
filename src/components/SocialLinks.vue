<template>
  <a :href="link" target="_blank" :class="customClass" class="social-link">
    <q-icon :class="'mdi ' + icon" :size="iconSize" />
  </a>
</template>

<script lang="ts">
  import { defineComponent } from 'vue';

  export default defineComponent({
    name: 'SocialLinks',
    props: {
      link: {
        type: String
      },
      icon: {
        type: String
      },
      iconSize: {
        type: String,
        default: 'md'
      },
      customClass: {
        type: String
      }
    }
  });
</script>
