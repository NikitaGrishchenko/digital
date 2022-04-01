import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/Index.vue') }]
  },
  {
    path: '/',
    component: () => import('layouts/SecondLayout.vue'),
    children: [
      {
        name: 'articleList',
        path: 'article/list',
        component: () => import('pages/Article/ArticleList.vue')
      },
      {
        name: 'articleDetail',
        path: 'article/:articleId',
        component: () => import('pages/Article/ArticleDetails.vue')
      },
      {
        name: 'teamList',
        path: 'team',
        component: () => import('pages/Team.vue')
      },
      {
        name: 'projectsList',
        path: 'projects',
        component: () => import('pages/Project.vue')
      },
      {
        name: 'loginPage',
        path: 'login',
        component: () => import('pages/Login.vue')
      }
    ]
  },
  {
    name: 'notFound',
    path: '/:catchAll(.*)*',
    component: () => import('src/pages/Error.vue')
  }
];

export default routes;
