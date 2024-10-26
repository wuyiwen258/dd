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
              <router-link to="/risk-check" class="nav-link active">Company Risk Check</router-link>
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
      <h2 class="text-center mb-4">Company Risk Check System</h2>
      <form @submit.prevent="searchRisks" class="d-flex justify-content-center flex-column align-items-center">
        <div class="search-container mb-3" style="width: 50%;">
          <input type="text" class="form-control" v-model="companyName" placeholder="Enter company name" required>
          <span class="clear-btn" @click="clearInput">&times;</span>
        </div>
        <button type="submit" class="btn btn-primary mt-4">Search</button>
      </form>

      <div v-if="results" id="resultsContainer" class="mt-5">
        <h3>Search Results for "{{ companyName }}"</h3>
        <table class="table table-bordered mt-3">
          <thead class="table-dark">
            <tr>
              <th>Risk Type</th>
              <th>Details</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(details, riskType) in results" :key="riskType">
              <td>{{ riskType }}</td>
              <td v-if="details.length > 0">
                <ul>
                  <li v-for="(detail, index) in details" :key="index">{{ detail }}</li>
                </ul>
              </td>
              <td v-else>No reported issues</td>
            </tr>
          </tbody>
        </table>
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
      results: null,
      errorMessage: ''
    };
  },
  methods: {
    clearInput() {
      this.companyName = '';
    },
    async searchRisks() {
      try {
        // 清空之前的错误信息和搜索结果
        this.errorMessage = '';
        this.results = null;

        // 调用后端 API
        const response = await axios.get('/api/search/check-risk', {
          params: {
            company_name: this.companyName
          }
        });

        // 将后端返回的数据赋值给 results
        if (response.data && response.data.results) {
          this.results = response.data.results;
        }
      } catch (error) {
        console.error('Error during risk search:', error);
        this.errorMessage = 'Unable to retrieve risk information. Please try again later.';
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
.table {
  width: 100%;
  margin-top: 20px;
}
.table-bordered th, .table-bordered td {
  border: 1px solid #dee2e6;
}
.table-dark {
  background-color: #343a40;
  color: white;
}
</style>
