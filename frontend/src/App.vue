<template>
  <div id="app">
    <router-view id="main"></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style lang="scss">
  body, html {
    margin: 0;
  }
  #app {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    #main {
      width: 100%;
      height: 100%;
      display: flex;
      flex-flow: column nowrap;
    }
  }
</style>
