<template>
  <q-page class="team-list">
    <div class="q-container">
      <PageTitle>Команда</PageTitle>
      <div
        v-if="isLoading || teammatesList.length === 0"
        class="row justify-center"
      >
        <div
          class="col-xl-4 col-md-6 col-sm-6 col-12 q-pa-md"
          v-for="index in 3"
          :key="index"
        >
          <div class="team-card__wrapper">
            <q-card class="team-card flex column justify-between">
              <q-card-actions align="center">
                <q-skeleton height="200px" width="200px" type="circle" />
              </q-card-actions>
              <q-card-section>
                <q-skeleton type="text" />
                <q-skeleton type="text" />
              </q-card-section>
            </q-card>
          </div>
        </div>
      </div>
      <div v-else class="row justify-center">
        <div
          class="col-xl-4 col-md-6 col-sm-6 col-12 q-pa-md"
          v-for="teammate in teammatesList"
          :key="teammate.id"
        >
          <div class="team-card__wrapper">
            <TeamCard :teammate="teammate" />
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script lang="ts">
  import { defineComponent, ref, onMounted } from 'vue';
  import { useTeam } from 'hooks/useTeam';
  import TeamCard from 'components/TeamCard.vue';
  import PageTitle from 'components/PageTitle.vue';
  import { Teammate } from '@types';

  export default defineComponent({
    name: 'TeamPage',
    components: {
      TeamCard,
      PageTitle
    },
    setup() {
      const { fetchTeammates } = useTeam();

      const teammatesList = ref<Teammate[]>([]);
      const isLoading = ref<boolean>(true);

      onMounted(() => {
        fetchTeammates()
          .then((teammates) => {
            teammatesList.value = teammates;
          })
          .finally(() => {
            isLoading.value = false;
          });
      });

      return {
        teammatesList,
        isLoading
      };
    }
  });
</script>
