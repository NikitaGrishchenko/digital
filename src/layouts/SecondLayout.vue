<template>
  <q-layout class="second-layout" view="lHh Lpr lFf">
    <Header shadow backgroundClass="bg-black" />
    <q-page-container>
      <CurvesBackground />
      <router-view v-slot="{ Component }">
        <transition
          appear
          enter-active-class="animated animate-duration-4 fadeInLeftBig"
          leave-active-class="animated animate-duration-4 fadeOutLeftBig"
        >
          <component :is="Component" />
        </transition>
      </router-view>
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
  import { defineComponent } from 'vue';
  import CurvesBackground from 'components/CurvesBackground.vue';
  import Header from 'layouts/Header.vue';

  export default defineComponent({
    name: 'SecondLayout',
    components: {
      CurvesBackground,
      Header
    }
  });
</script>
