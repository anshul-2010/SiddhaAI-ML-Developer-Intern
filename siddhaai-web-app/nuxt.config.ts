// https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({
  routeRules: {
    "/": { prerender: true },
    "/**": { ssr: true },
  },
  app: {
    head: {
      // link: [
      //   {
      //     rel: "stylesheet",
      //     href: "https://fonts.googleapis.com/css2?family=Montserrat&display=swap",
      //   },
      // ],
      htmlAttrs: {
        lang: "en",
      },
      title: "Siddhai Demo",
      meta: [
        {
          name: "author",
          content: "Bhaarat Krishnan",
        },
        {
          name: "description",
          content: "Siddhai Demo By Bhaarat Krishnan J",
        },
      ],
    },
    pageTransition: {
      name: "fade",
      mode: "out-in",
    },
    layoutTransition: {
      name: "fade",
      mode: "out-in",
    },
  },
  css: ["~/assets/css/main.css"],

  modules: [
    "@nuxtjs/tailwindcss",
    "nuxt-icon",
    "@morev/vue-transitions/nuxt",
    "@nuxtjs/google-fonts",
    "@pinia/nuxt"
  ],
});
