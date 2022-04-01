<template>
  <div :class="{ preserve: parallax }" ref="tiltComponent">
    <div :class="{ 'preserve-inner': parallax }">
      <slot></slot>
    </div>
  </div>
</template>
<script lang="ts">
  import { defineComponent, ref, onMounted, PropType } from 'vue';
  import VanillaTilt, { TiltOptions } from 'vanilla-tilt';

  export default defineComponent({
    name: 'TiltEffect',
    props: {
      options: Object as PropType<TiltOptions>,
      parallax: Boolean
    },
    setup(props) {
      const tiltComponent = ref<HTMLElement>();

      onMounted(() => {
        if (tiltComponent.value !== undefined)
          VanillaTilt.init(tiltComponent.value, props.options);
      });

      return {
        tiltComponent
      };
    }
  });
</script>

<style lang="sass" scoped>
  .preserve
    transform-style: preserve-3d
    transform: perspective(1000px)
    &-inner
      transform: translateZ(20px)
      height: 100%
</style>
