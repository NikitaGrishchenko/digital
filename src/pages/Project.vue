<template>
  <q-page class="project-list">
    <div class="q-container">
      <PageTitle>Наши проекты</PageTitle>

      <div
        v-if="isLoading || projectsList.length === 0"
        class="row justify-center"
      >
        <div
          class="col-xl-4 col-md-6 col-sm-6 col-12 q-pa-md"
          v-for="index in 3"
          :key="index"
        >
          <div class="project-card__wrapper">
            <q-card class="project-card">
              <q-skeleton height="200px" square />
              <q-card-section>
                <q-skeleton type="text" />
                <q-skeleton type="text" />
                <q-skeleton type="text" />
              </q-card-section>
            </q-card>
          </div>
        </div>
      </div>
      <div class="row justify-center">
        <div
          class="col-xl-4 col-md-6 col-sm-6 col-12 q-pa-md"
          v-for="project in projectsList"
          :key="project.id"
        >
          <div class="project-card__wrapper">
            <ProjectCard :project="project" />
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script lang="ts">
  import { defineComponent, ref, onMounted } from 'vue';
  import { Project } from '@types';
  import ProjectCard from 'components/ProjectCard.vue';
  import PageTitle from 'components/PageTitle.vue';
  import { useProject } from 'hooks/useProject';

  export default defineComponent({
    name: 'ProjectPage',
    components: {
      ProjectCard,
      PageTitle
    },
    setup() {
      const { fetchProjects } = useProject();

      const projectsList = ref<Project[]>([]);
      const isLoading = ref<boolean>(true);

      onMounted(() => {
        fetchProjects()
          .then((projects) => {
            projectsList.value = projects;
          })
          .finally(() => {
            isLoading.value = false;
          });
      });

      return {
        projectsList,
        isLoading
      };
    }
  });
</script>
