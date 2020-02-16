<template>
  <view class="container">
    <text class="text-color-primary">My Vue asds App</text>
  </view>
</template>

<script>
import login from './components/login';

export default {
  components: {
    login
  }
}
</script>

<style>
.container {
  background-color: white;
  align-items: center;
  justify-content: center;
  flex: 1;
}
.text-color-primary {
  color: blue;
}
</style>
