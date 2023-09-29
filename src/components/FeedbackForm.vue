<template>
    <q-dialog
        :progress="isSending"
        transition-show="slide-down"
        transition-hide="slide-up"
        position="top"
        ref="dialogRef"
        @hide="onDialogHide"
    >
        <q-card
            class="hide-scroll"
            style="min-width: 70%"
        >
            <q-form
                @submit.prevent="onSubmit"
                ref="feedbackForm"
                autofocus
                class="q-gutter-md"
            >
                <q-card-section class="bg-black text-white flex justify-between">
                    <div class="text-h6">Написать нам</div>
                    <q-btn
                        class=""
                        size="sm"
                        round
                        color="black"
                        icon="close"
                        @click="onCancelClick"
                    />
                </q-card-section>
                <q-card-section>
                    <q-input
                        class="q-pb-sm"
                        color="black"
                        outlined
                        hide-bottom-space
                        v-model="name"
                        label="Имя"
                        :rules="[(val) => !!val || 'Обязательное поле']"
                    >
                        <template v-slot:append>
                            <q-icon name="person" />
                        </template>
                    </q-input>
                    <q-input
                        class="q-pb-sm"
                        color="black"
                        outlined
                        hide-bottom-space
                        v-model="email"
                        label="Email"
                        type="email"
                        :rules="[(val) => !!val || 'Обязательное поле', isValidEmail()]"
                    >
                        <template v-slot:append>
                            <q-icon name="mail" />
                        </template>
                    </q-input>
                    <q-input
                        class="q-pb-sm hide-scroll"
                        color="black"
                        outlined
                        hide-bottom-space
                        v-model="appeal"
                        label="Обращение"
                        autogrow
                        :rules="[(val) => !!val || 'Обязательное поле']"
                    >
                        <template v-slot:append>
                            <q-icon name="question_answer" />
                        </template>
                    </q-input>
                </q-card-section>

                <q-separator />

                <q-card-actions align="between">
                    <Captcha />
                    <q-btn
                        :loading="isSending"
                        type="submit"
                        size="md"
                        color="black"
                        label="Отправить"
                    />
                </q-card-actions>
            </q-form>
            <q-inner-loading :showing="isSending">
                <q-spinner-gears
                    size="50px"
                    color="black"
                />
            </q-inner-loading>
        </q-card>
    </q-dialog>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useQuasar, useDialogPluginComponent, QForm } from 'quasar';
import { api } from 'boot/axios';
import Captcha from 'components/Captcha.vue';

export default defineComponent({
    name: 'FeedbackForm',
    components: { Captcha },
    emits: [...useDialogPluginComponent.emits],

    setup() {
        const $q = useQuasar();
        const { dialogRef, onDialogHide, onDialogCancel } =
            useDialogPluginComponent();

        const feedbackForm = ref<QForm>();
        let isSending = ref(false);
        const name = ref(''),
            email = ref(''),
            appeal = ref('');

        const isValidEmail = () => {
            const emailPattern =
                /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/;
            return (val: string) =>
                emailPattern.test(val) || 'Неверный формат Email';
        };

        const onSubmit = () => {
            void feedbackForm.value?.validate().then(async (success: boolean) => {
                if (success) {
                    isSending.value = true;
                    await api
                        .post('/feedback/create/', {
                            name: name.value,
                            email: email.value,
                            appeal: appeal.value
                        })
                        .then(() => {
                            dialogRef.value?.hide();
                            $q.notify({
                                timeout: 500,
                                type: 'positive',
                                progress: true,
                                message: 'Успешно отправлено!',
                                position: 'top-right'
                            });
                        })
                        .catch((e) => {
                            console.error(e);
                            $q.notify({
                                timeout: 500,
                                type: 'negative',
                                progress: true,
                                message: 'Ошибка соединения с сервером!',
                                position: 'top-right'
                            });
                        });
                    isSending.value = false;
                }
            });
        };
        return {
            name,
            email,
            appeal,
            isSending,
            isValidEmail,
            onSubmit,
            dialogRef,
            onDialogHide,
            onCancelClick: onDialogCancel,
            feedbackForm
        };
    }
});
</script>
