<template>
  <v-container id="icons" fluid tag="section">
    <base-material-card
      color="#283593"
      dark
      icon="mdi-chart-bubble"
      title="커뮤니티"
      class="px-5 py-3"
    >
      <br />
      <v-data-table
        :headers="headers"
        :items="desserts"
        :items-per-page="5"
        class="elevation-1"
        @click:row="rowClick"
        dark
      >
      </v-data-table>
      <br />
      <v-row>
        <v-btn v-if="token" outlined color="blue" @click="writeClick">
          작성
        </v-btn>
      </v-row>
    </base-material-card>
    <v-overlay :value="overlay">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
  </v-container>
</template>
<script>
import http from "@/util/http-common";
import { mapState } from "vuex";

export default {
  name: "Community",
  data() {
    return {
      headers: [
        {
          text: "Number",
          align: "left",
          sortable: false,
          value: "number",
        },
        { text: "Title", value: "title" },
        { text: "Username", value: "username" },
        { text: "Reg Date", value: "regDt" },
      ],
      desserts: [],
      overlay: true,
    };
  },
  created() {
    this.getCommunity();
  },
  computed: {
    ...mapState(["token"]),
  },
  methods: {
    getCommunity() {
      http
        .get("/community/community")
        .then((response) => {
          response.data.forEach((res) => {
            const r = new Date(res.created_at);
            const reg =
              "" +
              (r.getMonth() + 1) +
              "월 " +
              r.getDate() +
              "일 " +
              r.getHours() +
              ":" +
              r.getMinutes();
            this.desserts.push({
              number: res.id,
              username: res.user.username,
              title: res.title,
              regDt: reg,
            });
          });
          this.overlay=false
        })
        .catch((error) => {
          console.log(error);
        });
    },
    writeClick() {
      this.$router.push("/home/communityWrite");
    },
    rowClick(item) {
      this.$router.push({
        name: "CommunityDetail",
        params: { number: item.number },
      });
    },
  },
};
</script>
<style scoped>
.v-data-table /deep/ tbody /deep/ tr:hover{
  cursor:pointer !important;
}
</style>