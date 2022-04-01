<template>
  <div class="row">
    <div class="col-12 text-center">
      <h2 class="page-title q-my-md"><slot></slot></h2>
    </div>
  </div>
</template>

<script lang="ts">
  import { defineComponent } from 'vue';

  export default defineComponent({
    name: 'PageTitle'
  });
</script>
