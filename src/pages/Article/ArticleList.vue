<template>
  <!-- https://badcode.ru/ -->
  <!-- TODO при нажатии на tag с помощью route query показывать отфильтрованные статьи  -->
  <q-page class="article-list">
    <div class="row article-header flex items-center justify-center bg-black">
      <q-skeleton class="col-4 text-cente" v-if="isLoading" type="rect" />
      <div
        v-else-if="articlesList.length !== 0"
        class="col-4 text-center text-white"
      >
        <p v-if="'tag' in $route.query" class="article-tag">
          {{ $route.query.tag }}
        </p>
        <p v-else-if="'author' in $route.query" class="article-tag">
          {{ $route.query.author }}
        </p>
        <p v-else class="article-tag">Статьи</p>
        <p class="article-tag__count">
          Коллекция из {{ articlesList.length }} стат{{
            articlesList.length == 1 ? 'ьи' : 'ей'
          }}
        </p>
      </div>
      <div v-else class="col-4 text-center text-white">
        <p class="article-tag">Нет статей по данному запросу</p>
      </div>
    </div>
    <div class="q-container">
      <div v-if="isLoading" class="row justify-center article-cards">
        <div
          class="col-xl-4 col-lg-4 col-md-4 col-sm-6 col-xs-12 col-12 q-pa-md"
          v-for="index in 3"
          :key="index"
        >
          <q-card class="article-item__wrapper">
            <q-skeleton height="200px" square />
            <q-card-section>
              <q-skeleton type="text" />
              <q-skeleton type="text" />
              <q-skeleton type="text" />
            </q-card-section>
          </q-card>
        </div>
      </div>
      <div v-else class="row justify-center article-cards">
        <div
          class="col-xl-4 col-lg-4 col-md-4 col-sm-6 col-xs-12 col-12 q-pa-md"
          v-for="article in articlesList"
          :key="article.id"
        >
          <ArticleCard :article="article" />
        </div>
      </div>
    </div>
  </q-page>
</template>

<script lang="ts">
  import { useRoute } from 'vue-router';
  import { defineComponent, ref, onMounted, watch } from 'vue';
  import { useArticle } from 'hooks/useArticle';
  import { Article } from '@types';
  import ArticleCard from 'components/ArticleCard.vue';

  export default defineComponent({
    components: {
      ArticleCard
    },
    setup() {
      const route = useRoute();
      const { fetchArticlesList } = useArticle();

      const isLoading = ref<boolean>(true);
      const articlesList = ref<Article[]>([]);

      onMounted(() => {
        fetchArticlesList(route.query)
          .then((articles) => {
            articlesList.value = articles;
          })
          .finally(() => {
            isLoading.value = false;
          });
      });

      watch(
        () => route.query,
        () =>
          void fetchArticlesList(route.query).then((articles) => {
            articlesList.value = articles;
          })
      );

      return {
        isLoading,
        articlesList
      };
    }
  });
</script>
