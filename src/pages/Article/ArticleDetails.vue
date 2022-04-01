<template>
  <!-- https://badcode.ru/nachalo-raboty-s-axios-v-nuxt/ -->
  <!-- TODO есди dont_show_the_post true возвращать 404 -->
  <q-page class="article-details" v-if="articleDetail">
    <div class="row q-mt-xl flex justify-center">
      <div class="col-lg-8 col-10 flex justify-center">
        <div class="article-details__header">
          <p class="article-details__time-tag">
            {{
              new Date(articleDetail.dateOfPublication).toLocaleString('ru', {
                year: 'numeric',
                month: 'long',
                day: 'numeric'
              })
            }}
            <template v-if="articleDetail.tag">
              <span style="color: #738a94"> / </span>
              <router-link
                class="link__text-decoration"
                :to="{
                  name: 'articleList',
                  query: { tag: articleDetail.tag.name }
                }"
              >
                {{ articleDetail.tag.name }}
              </router-link>
            </template>
          </p>
          <p class="article-details__title">{{ articleDetail.name }}</p>
        </div>
        <img
          v-if="articleDetail.img"
          :src="articleDetail.img"
          alt
          class="article-details__img"
        />
        <img
          src="~images/Article.png"
          alt
          class="article-details__img"
          v-else
        />
      </div>
    </div>
    <div class="q-container article-container">
      <div class="row flex justify-center">
        <div
          class="
            col-lg-10 col-md-12 col-xs-12 col-12
            q-pa-xs-md q-pa-sm-md q-pa-md-lg q-pa-lg-xl
            rounded-borders
            shadow-1
            bg-white
          "
        >
          <div v-html="articleDetail.text"></div>
          <hr class="q-mt-md" />
          <div class="row article-details__footer flex justify-between">
            <div class="col-12 col-sm-6 col-md-6 col-lg-6 col-xl-3 q-pa-sm">
              <div class="article-details__numberOfViews flex items-center">
                <q-icon color="black" size="sm" class="mdi mdi-eye"></q-icon>
                <span class="q-ml-sm">{{ articleDetail.numberOfViews }}</span>
              </div>
            </div>
            <div
              class="
                col-12 col-sm-6 col-md-6 col-lg-6 col-xl-4
                q-mt-xs-md q-mt-sm-none
              "
            >
              <div
                class="article-details__authors flex justify-start items-center"
                v-for="author in articleDetail.author"
                :key="author.id"
              >
                <router-link
                  :to="{
                    name: 'articleList',
                    query: { author: author.username }
                  }"
                  class="flex items-center"
                >
                  <img
                    v-if="author.img"
                    :src="author.img"
                    alt=""
                    width="60"
                    height="60"
                    class="article-details__authors-img"
                  />
                  <img
                    v-else
                    width="60"
                    height="60"
                    class="article-details__authors-img__none"
                  />
                  <div class="article-details__authors-info q-ml-md">
                    <p class="article-details__authors-name">
                      {{ author.firstName }}
                      {{ author.lastName }}
                    </p>
                    <p class="article-details__authors-position">
                      {{ author?.position?.name }}
                    </p>
                  </div>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>
<script lang="ts">
  import _ from 'lodash';
  import { useArticle } from 'hooks/useArticle';
  import { defineComponent, ref, watch, onMounted, onUpdated } from 'vue';
  import { useRoute } from 'vue-router';
  import { Article } from '@types';
  import Prism from 'prismjs';
  import 'prismjs/themes/prism-tomorrow.css';

  export default defineComponent({
    setup() {
      const { fetchArticleDetails } = useArticle();
      const route = useRoute();
      const articleDetail = ref<Article>();

      onMounted(
        () =>
          !_.isNil(route.params.articleId) &&
          fetchArticleDetails(route.params.articleId[0]).then((article) => {
            articleDetail.value = article;
          })
      );

      onUpdated(() => {
        Prism.highlightAll();
      });

      watch(
        () => route.params.articleId,
        () =>
          !_.isNil(route.params.articleId) &&
          fetchArticleDetails(route.params.articleId[0]).then((article) => {
            articleDetail.value = article;
          })
      );

      return {
        articleDetail
      };
    }
  });
</script>
