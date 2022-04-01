<template>
  <q-layout class="main-layout" view="lHh Lpr lFf">
    <Header backgroundClass="bg-transparent" />
    <q-page-container>
      <CurvesBackground zIndex="1" />
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
  import Header from 'layouts/Header.vue';
  import CurvesBackground from 'components/CurvesBackground.vue';

  export default defineComponent({
    name: 'MainLayout',
    components: {
      CurvesBackground,
      Header
    }
  });
</script>

<style lang="sass" scoped>
  .q-page-container
    padding-top: 0 !important
    height: 100% !important
</style>
