<template>
  <div>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Company Search</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link to="/asic-search" class="nav-link">ASIC Company Search</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/risk-check" class="nav-link">Company Risk Check</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/australian-search" class="nav-link active">Australian Company Info</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <div class="container mt-5">
      <h2 class="text-center mb-4">Australian Company Search System</h2>
      <form @submit.prevent="searchCompany" class="d-flex justify-content-center">
        <div class="search-container" style="width: 50%;">
          <input type="text" class="form-control" v-model="companyName" placeholder="Enter company name or keyword" required>
          <span class="clear-btn" @click="clearInput">&times;</span>
        </div>
        <button type="submit" class="btn btn-primary ms-2">Search</button>
      </form>

      <!-- Display Results -->
      <div v-if="results.length > 0" class="mt-5">
        <h4 class="text-center mb-4">Search Results</h4>
        <div v-for="(company, index) in results" :key="index" class="card mb-4">
          <div class="card-body">
            <h5 class="card-title">{{ company.name }}</h5>
            <p class="card-text"><strong>Company ID:</strong> {{ company.id }}</p>
            <p v-if="company.established"><strong>Established:</strong> {{ company.established }}</p>
            <p v-if="company.links && company.links.length > 0"><strong>Links:</strong></p>
            <ul v-if="company.links && company.links.length > 0">
              <li v-for="(link, linkIndex) in company.links" :key="linkIndex">
                <a :href="link" target="_blank">{{ link }}</a>
              </li>
            </ul>
            <p v-if="company.locations && company.locations.length > 0"><strong>Locations:</strong></p>
            <ul v-if="company.locations && company.locations.length > 0">
              <li v-for="(location, locationIndex) in company.locations" :key="locationIndex">
                {{ location.join(', ') }}
              </li>
            </ul>
            <p v-if="company.relationships && company.relationships.length > 0"><strong>Relationships:</strong></p>
            <ul v-if="company.relationships && company.relationships.length > 0">
              <li v-for="(relationship, relationshipIndex) in company.relationships" :key="relationshipIndex">
                {{ relationship[0] }}: {{ relationship[1] }}
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div v-if="errorMessage" class="alert alert-danger mt-4 text-center">
        {{ errorMessage }}
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      companyName: '',
      results: [],
      errorMessage: ''
    };
  },
  methods: {
    clearInput() {
      this.companyName = '';
    },
    async searchCompany() {
      try {
        // 清空之前的错误信息和搜索结果
        this.errorMessage = '';
        this.results = [];

        // 调用后端 API
        const response = await axios.get('/api/search/australian', {
          params: { query: this.companyName }
        });

        // 将后端返回的数据赋值给 results
        if (response.data && response.data.results) {
          this.results = response.data.results;
        }
      } catch (error) {
        console.error('Error during company search:', error);
        this.errorMessage = 'Unable to retrieve company information. Please try again later.';
      }
    }
  }
};
</script>

<style scoped>
.search-container {
  position: relative;
}
.clear-btn {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
  font-size: 20px;
  color: gray;
  display: none;
}
.form-control:valid ~ .clear-btn {
  display: block;
}
.card {
  border: 1px solid #ddd;
  padding: 20px;
}
.card-title {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}
.card-text {
  margin-bottom: 0.5rem;
}
</style>

