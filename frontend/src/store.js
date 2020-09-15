import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        user_id: '',
        user_jwt: '',
        user_name: '',
        user_point: '',
        user_image: '',
        user_grade: '',
        base_url: '',
        search_word: ''
    },
    plugins: [createPersistedState()],
    mutations: {
        urlSave(state, url) {
            state.base_url = url
        },
        idSave(state, id) {
            state.user_id = id
        },
        jwtSave(state, jwt) {
            state.user_jwt = jwt
        },
        nameSave(state, name) {
            state.user_name = name
        },
        pointSave(state, point) {
            state.user_point = point
        },
        wordSave(state, word) {
            state.search_word = word
        },
        imgSave(state, img) {
            state.user_image = img
        },
        gradeSave(state, grade) {
            state.user_grade = grade
        }
    },
    actions: {

    }
})
