<template>
  <div class="row">
    <div class="col-12 text-center">
      <h2 class="page-title q-my-md">
        <q-form
          ref="loginForm"
          @submit.prevent="onSubmit()"
          class="login-form--wrapper"
        >
          <q-input
            class="login-form__input login-form__input--top"
            borderless
            type="text"
            v-model="usernameModel"
            :rules="[(val) => !!val]"
            label="Логин"
          />
          <q-input
            class="login-form__input login-form__input--bottom"
            borderless
            :type="isPassword ? 'password' : 'text'"
            v-model="passwordModel"
            :rules="[(val) => !!val]"
            label="Пароль"
          >
            <template v-slot:after>
              <q-icon
                :name="isPassword ? 'mdi-eye-off' : 'mdi-eye'"
                class="cursor-pointer"
                @click="isPassword = !isPassword"
              />
            </template>
          </q-input>

          <q-btn
            class="q-my-md login-form__btn"
            label="Войти в систему"
            type="submit"
            color="primary"
          >
            <q-icon name="mdi-login q-ml-xs" size="15px" />
          </q-btn>

          <q-inner-loading :showing="false">
            <q-spinner-gears size="50px" color="primary" />
          </q-inner-loading>
        </q-form>
      </h2>
    </div>
  </div>
</template>

<script setup lang="ts">
  // import { AxiosError } from 'axios';
  import { useAuth } from 'hooks/useAuth';
  import { QForm } from 'quasar';
  import { ref } from 'vue';

  // const serverErrors = ref<string[]>([]);

  const usernameModel = ref<string>('');
  const passwordModel = ref<string>('');

  const loginForm = ref<QForm>();

  const isPassword = ref<boolean>(true);
  // const errorModal = ref<boolean>(false);

  const { userLogin } = useAuth();

  // const resetForm = () => {
  //   loginForm.value?.resetValidation();
  //   serverErrors.value = [];
  // };

  const onSubmit = async () => {
    await userLogin(usernameModel.value, passwordModel.value);
  };
</script>
