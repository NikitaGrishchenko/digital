<template>
  <q-btn icon="menu">
    <q-menu transition-show="jump-down" transition-hide="jump-up">
      <q-list>
        <template v-if="links !== undefined">
          <q-item
            v-for="link in links"
            :key="link.id"
            :to="link.link"
            clickable
            v-close-popup
          >
            <q-item-section>{{ link.title }}</q-item-section>
          </q-item>
        </template>
        <template v-if="actions !== undefined">
          <q-item
            v-for="action in actions"
            :key="action.id"
            clickable
            v-close-popup
            @click="action.func"
          >
            <q-item-section>{{ action.title }}</q-item-section>
          </q-item>
        </template>
      </q-list>
    </q-menu>
  </q-btn>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';

type link = {id:number, link: string, title: string};
type action = {id:number, func: VoidFunction, title: string};

export default defineComponent({
  props: {
    links: {
      type: Object as PropType<link[]>,
      required: false,
    },
    actions: {
      type: Object as PropType<action[]>,
      required: false,
    },
  },
  setup() {
    return {};
  },
});
</script>
