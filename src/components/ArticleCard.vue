<template>
  <q-card @click="openToDetail(article.id)" class="article-item__wrapper">
    <img v-if="article.img" :src="article.img" class="article-item__img" />
    <img v-else src="~images/Article.png" class="article-item__img" />
    <q-card-section>
      <p v-if="article.tag" class="article-item__tag">
        {{ article?.tag?.name }}
      </p>
      <div class="article-item__title">{{ article.name }}</div>
      <div class="article-item__preview">
        <div class="v-html" v-html="article.preview"></div>
      </div>
    </q-card-section>
  </q-card>
</template>

<script lang="ts">
  import { defineComponent, PropType } from 'vue';
  import { useRouter } from 'vue-router';
  import { Article } from '@types';

  export default defineComponent({
    name: 'Article',
    props: {
      article: {
        type: Object as PropType<Article>,
        required: true
      }
    },
    setup() {
      const router = useRouter();
      const openToDetail = (articleId: number) => {
        void router.push({
          name: 'articleDetail',
          params: { articleId: articleId }
        });
      };
      return {
        openToDetail
      };
    }
  });
</script>
