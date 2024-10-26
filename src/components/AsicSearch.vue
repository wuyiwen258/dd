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
              <router-link to="/asic-search" class="nav-link active">ASIC Company Search</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/risk-check" class="nav-link">Company Risk Check</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/australian-search" class="nav-link">Australian Company Info</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <div class="container mt-5">
      <h2 class="text-center mb-4">ASIC Company Search System</h2>
      <form @submit.prevent="searchCompany" class="d-flex justify-content-center">
        <div class="search-container" style="width: 50%;">
          <input type="text" class="form-control" v-model="companyName" placeholder="Enter company name" required>
          <span class="clear-btn" @click="clearInput">&times;</span>
        </div>
        <button type="submit" class="btn btn-primary ms-2">Search</button>
      </form>

      <table class="table table-bordered mt-5" v-if="results.length > 0">
        <thead class="table-dark">
          <tr>
            <th>Company Name</th>
            <th>ABN</th>
            <th>Status</th>
            <th>Registration Date</th>
            <th>Registered Address</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(company, index) in results" :key="index">
            <td>{{ company.name }}</td>
            <td>{{ company.abn }}</td>
            <td>{{ company.status }}</td>
            <td>{{ company.registration_date }}</td>
            <td>{{ company.registered_address }}</td>
          </tr>
        </tbody>
      </table>

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
        const response = await axios.get('/api/search/asic', {
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
</style>

