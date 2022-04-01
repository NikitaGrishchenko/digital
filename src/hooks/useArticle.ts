import { api } from 'boot/axios';
import { Article } from '@types';
import { LocationQuery } from 'vue-router';

export function useArticle() {
  const fetchArticlesList = (query: LocationQuery): Promise<Article[]> => {
    return new Promise((resolve, reject) => {
      api
        .get<Article[]>('article/list/', { params: query })
        .then((response) => {
          resolve(response.data);
        })
        .catch((error) => {
          console.error(error);
          reject(error);
        });
    });
  };

  const fetchArticleDetails = (
    articleId: number | string
  ): Promise<Article> => {
    return new Promise((resolve, reject) => {
      api
        .get<Article>(`article/details/${articleId}`)
        .then((response) => {
          resolve(response.data);
        })
        .catch((error) => {
          console.error(error);
          reject(error);
        });
    });
  };

  return {
    fetchArticlesList,
    fetchArticleDetails
  };
}
