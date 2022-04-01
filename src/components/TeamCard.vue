<template>
  <TiltEffect
    :options="{
      max: $q.screen.lt.sm ? 0 : 15
    }"
    :parallax="true"
  >
    <q-card
      class="
        team-card
        text-center
        flex
        column
        justify-start
        items-center
        q-pa-md
      "
    >
      <q-intersection once>
        <q-avatar size="200px" v-if="teammate.img" key="main-image">
          <img :src="teammate.img" alt class="team-card__img" />
        </q-avatar>
        <q-avatar
          v-else
          key="second-image"
          size="200px"
          color="black"
          text-color="white"
          icon="mdi-account"
          class="team-card__img"
        />
      </q-intersection>
      <q-intersection once>
        <div class="team-card__content">
          <q-card-section>
            <p class="team-card__fullname">
              {{ teammate.firstName }}
              {{ teammate.lastName }}
            </p>
            <div class="team-card__position">
              {{ teammate?.position?.name }}
            </div>
          </q-card-section>
          <q-card-section>
            <div class="team-card__social">
              <SocialLinks
                customClass="text-black"
                v-for="social in teammate.social"
                :key="social.id"
                :link="social.link"
                :icon="social.icon"
              />
            </div>
          </q-card-section>
        </div>
      </q-intersection>
    </q-card>
  </TiltEffect>
</template>

<script lang="ts">
  import TiltEffect from 'components/TiltEffect.vue';
  import SocialLinks from 'components/SocialLinks.vue';
  import { defineComponent, PropType } from 'vue';
  import { Teammate } from '@types';

  export default defineComponent({
    name: 'TeamCard',
    components: {
      TiltEffect,
      SocialLinks
    },
    props: {
      teammate: {
        type: Object as PropType<Teammate>,
        required: true
      }
    }
  });
</script>
