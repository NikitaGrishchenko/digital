<template>
  <div
    class="fullscreen bg-blue text-white text-center q-pa-md flex flex-center"
  >
    <div>
      <div style="font-size: 30vh">
        {{ code }}
      </div>

      <div class="text-h2" style="opacity: 0.4">
        <slot>Страница не найдена</slot>
      </div>

      <q-btn
        class="q-mt-xl"
        color="white"
        text-color="blue"
        unelevated
        to="/"
        label="На главную"
        no-caps
      />
    </div>
  </div>
</template>

<script lang="ts">
  import { defineComponent } from 'vue';

  export default defineComponent({
    name: 'Error',
    props: {
      code: {
        type: String,
        default: '404'
      }
    }
  });
</script>
