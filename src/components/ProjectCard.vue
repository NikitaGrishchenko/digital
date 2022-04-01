<template>
  <TiltEffect
    class="full-height"
    :options="{
      max: $q.screen.lt.sm ? 0 : 15
    }"
    :parallax="true"
  >
    <q-card
      @click="toProjectPage"
      class="project-card flex column items-center cursor-pointer"
    >
      <img
        v-if="project.img"
        :src="project.img"
        alt
        class="project-card__img"
      />
      <img v-else src="~images/Article.png" alt class="project-card__img" />
      <q-space />
      <q-card-section class="q-pa-lg">
        <p class="project-card__name">
          {{ project.name }}
        </p>
        <div class="project-card__description">
          {{ project?.description }}
        </div>
      </q-card-section>
      <q-space />
    </q-card>
  </TiltEffect>
</template>

<script lang="ts">
  import TiltEffect from 'components/TiltEffect.vue';
  import { defineComponent, PropType } from 'vue';
  import { Project } from '@types';

  export default defineComponent({
    name: 'ProjectCard',
    components: {
      TiltEffect
    },
    props: {
      project: {
        type: Object as PropType<Project>,
        required: true
      }
    },
    setup(props) {
      const toProjectPage = (): void => {
        window.open(props.project.link, '_blank');
      };

      return {
        toProjectPage
      };
    }
  });
</script>
