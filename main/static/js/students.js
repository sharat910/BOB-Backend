new Vue({
   el: '#students',
   delimiters: ['${','}'],
   data: {
   articles: [],
   loading: false,
   currentArticle: {},
   message: null,
   newArticle: { 'article_heading': null, 'article_body': null },
 },
 mounted: function() {
 this.getArticles();
},
methods: {
 getArticles: function() {
  this.loading = true;
  this.$http.get('/api/student/')
      .then((response) => {
        this.articles = response.data;
        this.loading = false;
      })
      .catch((err) => {
       this.loading = false;
       console.log(err);
      })
 },
 getArticle: function(id) {
  this.loading = true;
  this.$http.get('/api/student/${id}/')
      .then((response) => {
        this.currentArticle = response.data;
        this.loading = false;
      })
      .catch((err) => {
        this.loading = false;
        console.log(err);
      })
 },
 addArticle: function() {
  this.loading = true;
  this.$http.post('/api/student/',this.newArticle)
      .then((response) => {
        this.loading = false;
        this.getArticles();
      })
      .catch((err) => {
        this.loading = false;
        console.log(err);
      })
 },
 updateArticle: function() {
  this.loading = true;
  this.$http.put('/api/student/${this.currentArticle.article_id}/',     this.currentArticle)
      .then((response) => {
        this.loading = false;
        this.currentArticle = response.data;
        this.getArticles();
      })
      .catch((err) => {
        this.loading = false;
        console.log(err);
      })
 },
 deleteArticle: function(id) {
  this.loading = true;
  this.$http.delete('/api/student/${id}/' )
      .then((response) => {
        this.loading = false;
        this.getArticles();
      })
      .catch((err) => {
        this.loading = false;
        console.log(err);
      })
 }
 }
});