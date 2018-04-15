<template>

  <div id="container" @dblclick="snapshot">
    <v-toolbar color="blue">
      <v-toolbar-title class="white--text">Undefined</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <video id="video"></video>
    <div id="cards">
      <v-card id="card" v-for="item in cards">
        {{item}}
      </v-card>
    </div>
    <v-btn fab dark large color="purple" @click="snapshot1" id="play_btn1">

     <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAALjSURBVFhH7ZZbaI5xHMffHTCHkeWwRNokhywjrpCzi+29WHKImuRCrXajMDcuhNIu1FJKDkVJRKSknJILOcZWSC5oc7GRmcPCZu/r8/33e/SS7X2eZ89TLvatT//f//87Pe/z/t//+08MKIxSqdRQWJ5Op1dkMMLc8Yvme2j4h1g7aO54Ra9cmjVDnS1pbSvz94yDbSk+0agCumE8TIHJUAhfYL2FxSeanIeLZt/nU982+zhclx2baDAOfkCSxtNB330PTIIFZpdYePSi+HZ4S998xn3QBG+Y7zL/M6274DhE8Rewn4Y5agw71RCazL8NWvDnuYQoRdGFFE8xljIsBr3uiTCTNX0VsxnGMOorqrS06ETRE3DL7KNw0zkQjR8xrzf7HLbbpJGJgiPhK2ykQQF0wGZzZ756nRGroBu72Nz9F8V00LQzFjCug04oNLf8xcx/wjJ7iNeMbmNGIgo+gENmX4YzzpEh1q7CMbN3wyseIsc5+yMKlVFIKsceC11QYe7fYq0aPhGnt6RzQZt0qbnDiyIN8NDsWmijSb5zZoj14aB9ssbmV+C0c4YVBYbAB6ix+TXQ/0B7L2gfnLTY1fANijQPJZI3QCefeJTN9XWs7QtipioWexB2K9RqHkok34BTsik4Gkr9QI77hTDWQ6PswCKxBLSRFlFUZ79+575ErLdnpoE03xUNIpL2wkvq6dzXHaALuxz++ak9iFvJqIcoszp34Igr6lfk55HUAu7Ww3gWLjmnDxHbSI0DZuvn+Zm5/zsjCZXgjlPGIviOXWXurCJ+BzSTkwvDoIP5FnNnF8EXwLv11MA7ivi+7xE/AXrIWWLzw3DXObOJQN31dNolbX4PGpwzgMjRmeEdzXN5GO2LWc7ZlwjS6/NuPTMscY65fYucTeCOZps/huxXd4KewEcS9R+vW89TcwUSebop62h+brXaoNXcvYvgKgLrMphnrsAiN/lXrWpzDeh/USLxCydQCi93gTpXAAAAAElFTkSuQmCC"></img>
    </v-btn>
        <v-btn fab dark large color="purple" @click="snapshot2" id="play_btn2">
     <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANmSURBVFhH1ZdLSBZRGIa9lFJgId0UjIhCVyEUEQhJC0GpbOMmqAhJ6OLCaCMuBMNFrbKFUhsNN0FSQXbbdaG0RVAUbQyKLrjIoEILNPW35zvzjre5/X+48YGXc+b93vNNM3Ocf8paVqRSqU2oAV1GN9AzdB/1zMzMtDFWMuYqvjTQMJvGdWgQTXMcC5nvqBMVq8X/Q5M96IV6z4L3AdnV30T30Gs0qrKD49+oHeWrXWawsB6Nq581HEJNaKsiCyCSR60a9aBJb5Vb9xxtVCw9WNfmLXcNfqDTTFeonAj5MnTX6+B6fEbbVY6HYL3W+VddqlJGsNz2TitKqddbhrUqh0PInvmEFrxnKFRpAfjW/CS6zfwiimxMxu6eg/kt2UGoW1N/w/1iHnnLqDUq5+C4X6VQqHcqatn9shdCoU4ZC52SHQr1h4o6OP7LkKdyAOr56JOy9ihyVJqDwoACQwyxG47MA8suYqXKobDmqHJ2jhrZHnhFmO4lw9gkOxIy3Zb14XhMpUiI5ZL7pvwV2R4YDVYwmIf+nc+HzDnFHRy/USkWcvbKtvywLA+MDhU+yoqFXIXlfTjuVikWcvMfQ4lsd3v6ZD6VFQs521Szr17mJ1SKheg+b4VbUyHbFZ549kyfrEQsawtoZHunSHYsZEttjcH8gGxXcLvaRlmJkD2uNYOyEiG+y9aIKtmumdvVjK9kJUK8kLz9TjTKSoRsrZ3HYF4u2xXOyxxDaf98ki3QNC3IN+s8UwyrZbuCfck4mFfLXnLo7b/sHsnywLOXxIiK12THQm4NOox2y4qF3Bbkv+zOyp4Ds0vFSVQmOxIyL5U3amVHQqZX+XG0WfYcmMXoj0L9DNkqBaBmXz/ud95gekGlUKjbz7x/9R2yg1Bsdx2BeavsUKhfV24URT4GIvY781XZn2idSkHI2JX5G8U4o1IAIvb9sINxvawA1O2u+o9qGh1SKRpCG9AXW2Qw70IZf9myxm67u3KDeYtKyRDeht5prS22j8ojTBP/00HOdnsv8p+5XXkL08g9FQqLCtAda+LD8QjqRsdQJbKv353oIGpGA8id2GBuzzz5tsdBgxpkn1FpQ34CXWIauT8ygkY5+odcRcPuLIvAn0KPkf3nJfh3vpRwghK0F1Vz7irGcrRK5eVEVtY/QZZaS2urNTcAAAAASUVORK5CYII="></img>
    </v-btn>
        <v-btn fab dark large color="purple" @click="snapshot3" id="play_btn3">
        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAALpSURBVFhH7ZVLSFVRFIZvWV6vaQ+0NAgSMUhMEsuoQUSjJEgqKCQUosJZL7AGjRo0igQznBUSRFCDsqKnEFFgBA5C0qB8Qe+IIrJSqXv7/u26G09JpdlAOD987L3+tc4+5+519rmRUKFCTTolEonp8Xh8CeNGxiqohHLiPCuZeHGDGDfYwngWPjB3Yv4O+i1U3Av1sIZwil0+frFIBovVwmuQzuFth3xItTI94AziEsYDcJ+5HuYhbGY61crGJi7W1r4B94sZGyzlhZ2PP9dCJ+IotEM/DFLTBiWW/rO4KAsuwDdohG3wBbKsRDXF0KEHk5g3M8yytPIbYABWwS0YIn8YUqxkdFFYCupjD6ww7zhccwWIuX7hU914pPCarEQ7k0qsHdikmLEaPkEL+B8SEIn18Bkus8Bss+VfgnoLFZe5O/4k/I8Mvt/EasM+C/VQi4kfwxPmwRODoSM1BCeZB7YJrxl8/5mXUvOL8N8z+DefuAP8A0jks6EN/wUUJE29vYPQMHKBpPDVghYLVT+NuJ0xILxGK1FNGrFaUGGWF95MaIU+iKo4l8kzuAuZVueFVw56iXLNklcA9+zG2rkmpumWVn4rDOBlmOWFXwgv4Sb54R9MsAieQytmtjNNxCn4j+C0WV7k5kCahU7E6dSq1yfM8sJbDjrat1Vn9rAwF0IndMFSs52IV4PadNCsUUU+BlegGwJvO7E7ztz4PGPU7KBIqD8X4Svspdi/1cz1KZavl7LIbCfV4alVevPVW59nngmnQN+VQ9T+/hOtAgp3g87tA1hpKeWWESd7r526zvQOo7b1O+hG7sto6+j8q9/akbVukb8VC+Rxkb4BWvgGrMNzO8K8CPbAMTgCOyDHcvrjqmHUMdSOHSUO9nss4mL9arVFW/gWzsAu0IdLn+QyqID9cBX0MdMRrIP5tsy/i8XmwU7QrrziwbyItUtqiVqg/4GYXfb/xH31V70AcpgHjmKoUKEmkSKRH+S/+wUHgS/xAAAAAElFTkSuQmCC"></img>   
    </v-btn>
  </div>
</template>

<script>
import api from '../api';

export default {
  name: 'HelloWorld',
  data() {
    return {
      translated: '',
      cards: [],
      readingList: [],
      curRead: 0,
      playing: false,
    };
  },
  mounted() {
    // Grab elements, create settings, etc.
    const video = document.getElementById('video');

    // Get access to the camera!
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      // Not adding `{ audio: true }` since we only want video now
      navigator.mediaDevices.getUserMedia({ video:true  }).then((stream) => {
        video.src = window.URL.createObjectURL(stream);
        video.play();
      });

    }
  },
  methods: {
    snapshot1(){
      this.snapshot('w');
    },
    snapshot2(){
      this.snapshot('d');
    },
    snapshot3(){
      this.snapshot('c');
    },
    snapshot(action) {
      const canvas = (this.canvas = document.createElement('canvas'));
      const context = canvas.getContext('2d');
      const video = document.getElementById('video');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      context.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);

      this.playing = false;
      this.curRead = 0;
      this.readingList = [];
      this.imageCaption(action);
    },

    playCurAudio() {
      const audio = document.createElement('audio');
      if (this.curRead >= this.readingList.length || this.playing) {
        return;
      }
      this.playing = true;
      audio.src = this.readingList[this.curRead++];
      audio.play();

      audio.onended = () => {
        if (this.curRead < this.readingList.length || !this.playing) {
          audio.src = this.readingList[this.curRead++];
          audio.play();
        } else {
          this.playing = false;
        }
      };
    },

    translate(text) {
      api.translate(text, 'en-zh').then((res) => {
        this.translated = res.data.translation[0];
        this.cards.push(res.data.translation[0]);
        this.readingList.push(res.data.tSpeakUrl);
        this.playCurAudio();
      }).catch((err) => {
        alert(err);
      });
    },

    imageCaption(action) {
      this.canvas.toBlob(
        (data) => {
          api.imageCaption(data,action).then((res) => {
            this.cards.push(res.data.c.caption);
            this.translate(res.data.c.caption);

            this.cards.push(res.data.d);
            this.translate(res.data.d);
            setTimeout(()=>document.querySelector("#cards").scrollTo(0,10000000000),100);
            console.log(res.data);
          });
        },
        'image/jpeg',
        1,
      );
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  #container {
    display: flex;
    flex-flow: row nowrap;
    height: 100%;
    width: 100%;
    overflow-y: hidden;
  }
  #video {
    width: 100vw;
    max-height: 50vh;
  }
  #play_btn {
    position: absolute;
    z-index: 9999;
    right:10px;
    bottom: 10px;
    display: flex;
    flex-flow: row nowrap;
    justify-content: center;
    align-items: center;
    img {
      width: 50%;
      height: 50%;
    }
  }  #play_btn1 {
    position: absolute;
    z-index: 9999;
    right:10px;
    bottom: 10px;
    display: flex;
    flex-flow: row nowrap;
    justify-content: center;
    align-items: center;
    img {
      width: 50%;
      height: 50%;
    }
  }
    #play_btn2 {
    position: absolute;
    z-index: 9999;
    right:100px;
    bottom: 10px;
    display: flex;
    flex-flow: row nowrap;
    justify-content: center;
    align-items: center;
    img {
      width: 50%;
      height: 50%;
    }
  }
    #play_btn3 {
    position: absolute;
    z-index: 9999;
    right:200px;
    bottom: 10px;
    display: flex;
    flex-flow: row nowrap;
    justify-content: center;
    align-items: center;
    img {
      width: 50%;
      height: 50%;
    }
  }
  #cards {
    flex-grow: 0;
    overflow-y: auto;
    #card {
      margin: 1rem;
      padding: 1rem;
      display: flex;
      flex-flow: column wrap;
    }
  }
</style>
