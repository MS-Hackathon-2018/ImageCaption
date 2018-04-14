<template>
  <el-container>
    <el-header>
    </el-header>
    <el-main>
      <el-row>
        <el-col :span="12">
          <video id="video"></video>
        </el-col>
        <el-col :span="12">
          <canvas id="snapshot"></canvas>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="24">
          <el-input :value="caption">

          </el-input>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="24">
          <el-button @click="snapshot">
            拍照
          </el-button>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="12">
          <el-input v-model="text">

          </el-input>
        </el-col>

        <el-col :span="12">
          <el-input :value="translated" :disabled="true">

          </el-input>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="12">
          <el-button @click="translate">
            翻译
          </el-button>
        </el-col>
        <el-col :span="8">
          <audio id="audio" controls="controls">

          </audio>
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
import api from '../api';
import ElInput from "element-ui/packages/input/src/input";

export default {
  components: {ElInput},
  name: 'HelloWorld',
  data() {
    return {
      text: '',
      translated: '',
      lastOutput: {},
      caption: '',
    };
  },
  mounted() {
    // Grab elements, create settings, etc.
    const video = document.getElementById('video');

    // Get access to the camera!
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      // Not adding `{ audio: true }` since we only want video now
      navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
        video.src = window.URL.createObjectURL(stream);
        video.play();
      });
    }
  },
  methods: {
    snapshot() {
      const canvas = document.getElementById('snapshot');
      const context = canvas.getContext('2d');
      const video = document.getElementById('video');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      context.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);

      this.imageCaption();
    },

    translate() {
      const audio = document.getElementById('audio');
      api.translate(this.text, 'en-zh').then((res) => {
        this.lastOutput = res.data;
        this.translated = res.data.translation[0];
        audio.src = res.data.tSpeakUrl;
        audio.play();
      }).catch((err) => {
        alert(err);
      });
    },

    imageCaption() {
      const canvas = document.getElementById('snapshot');
      canvas.toBlob((data) => {
        api.imageCaption(data).then((res) => {
          this.caption = res.data.caption;
          this.text = this.caption;
          this.translate();
        });
      }, 'image/jpeg', 1);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  #container {
    #snapshot {
      width: 100% !important;
      height: 100% !important;
    }
  }
</style>
