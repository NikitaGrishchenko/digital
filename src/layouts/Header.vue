<template>
    <q-header
        :elevated="shadow"
        :class="backgroundClass"
    >
        <q-toolbar class="bg-transparent q-pa-md">
            <router-link
                :to="{ path: '/' }"
                class="flex items-center"
            >
                <img src="~assets/images/digital.png" />
            </router-link>
            <q-space />
            <template v-if="$q.screen.gt.xs">
                <router-link
                    v-for="link in linksList"
                    :key="link.id"
                    :to="link.link"
                    class="second-layout__link text-white link__text-decoration"
                    active-class="second-layout__link--active"
                    stretch
                    flat
                >{{ link.title }}</router-link>
            </template>
            <q-btn
                unelevated
                color="primary"
                label="Написать нам"
                @click="showFeddbackForm"
                class="second-layout__menu"
            />
        </q-toolbar>
    </q-header>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useQuasar } from 'quasar';
import FeedbackForm from 'components/FeedbackForm.vue';

export default defineComponent({
    components: {
        // SocialLinks,
        // Menu
    },
    props: {
        shadow: {
            type: Boolean,
            default: false
        },
        backgroundClass: {
            type: String,
            default: 'bg-black'
        }
    },
    setup() {
        const $q = useQuasar();
        const showFeddbackForm = () => {
            $q.dialog({
                component: FeedbackForm
            });
        };

        const linksList = [
            {
                id: 0,
                title: 'Статьи',
                link: { name: 'articleList' }
            },
            {
                id: 1,
                title: 'Команда',
                link: { name: 'teamList' }
            },
            {
                id: 2,
                title: 'Наши проекты',
                link: { name: 'projectsList' }
            },
            // {
            //   id: 3,
            //   title: 'Авторизоваться',
            //   link: { name: 'loginPage' }
            // }
        ];
        const actionsList = [
            {
                id: 0,
                title: 'Связаться',
                func: showFeddbackForm,
                class: 'second-layout__menu'
            }
        ];
        return {
            showFeddbackForm,
            actionsList,
            linksList,
            // socialsList
        };
    }
});
</script>
