<template>
  <div>
    <transition
      appear
      enter-active-class="animated animate-duration-4 fadeInLeftBig"
      leave-active-class="animated animate-duration-4 fadeOutLeftBig"
    >
      <div class="flex row no-wrap" v-if="!isValid">
        <q-img
          @click="zoomImage"
          style="cursor: zoom-in"
          class="q-mr-md"
          width="100%"
          fit="contain"
          :src="captcha?.image"
        >
          <template v-slot:error>
            <div class="absolute-full flex flex-center bg-negative text-white">
              Ошибка соединения с сервером
            </div>
          </template>
        </q-img>
        <q-input
          v-model="userAnswer"
          label="Ответ"
          color="black"
          no-error-icon
          hide-bottom-space
          @update:model-value="captchaIsValid"
          ref="captchaInput"
          :disable="isValid"
          :rules="[
            (val) => !!val || 'Обязательное поле',
            () => isValid || 'Неверно'
          ]"
        >
          <template v-slot:append>
            <q-icon
              class="cursor-pointer"
              @click="refreshCaptcha"
              name="refresh"
            />
          </template>
        </q-input>
      </div>
    </transition>
  </div>
</template>

<script lang="ts">
  import { defineComponent, onMounted, ref } from 'vue';
  import { useCaptcha } from 'hooks/useCaptcha';
  import { Captcha } from '@types';
  import { useQuasar, QInput } from 'quasar';

  export default defineComponent({
    name: 'Captcha',
    setup() {
      const { fetchCaptcha, sendCaptcha, updateCaptcha } = useCaptcha();
      const $q = useQuasar();

      const userAnswer = ref<string>('');
      const isValid = ref<boolean>(false);
      const captcha = ref<Captcha>();
      const captchaInput = ref<QInput>();

      const captchaIsValid = () => {
        captcha.value &&
          userAnswer.value.length === 5 &&
          sendCaptcha(captcha.value.uuid, userAnswer.value)
            .then(() => {
              isValid.value = true;
            })
            .catch(() => {
              isValid.value = false;
            });
      };

      const refreshCaptcha = () => {
        captcha.value &&
          void updateCaptcha(captcha.value.uuid).then((response) => {
            captchaInput.value?.resetValidation();
            captcha.value = response.data;
            captchaInput.value?.focus();
          });
      };
      const zoomImage = () => {
        captcha.value &&
          $q.dialog({
            ok: false,
            message: `<img class="w-100" src=${captcha.value?.image} />`,
            html: true
          });
      };

      onMounted(() => {
        void fetchCaptcha().then((response) => {
          captcha.value = response.data;
        });
      });
      return {
        userAnswer,
        captcha,
        sendCaptcha,
        captchaIsValid,
        refreshCaptcha,
        zoomImage,
        isValid,
        captchaInput
      };
    }
  });
</script>
