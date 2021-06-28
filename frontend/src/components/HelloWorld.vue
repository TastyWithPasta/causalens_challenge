<template>
  <div class="helloworld">
    <h1 class="title">Causalens Challenge</h1>
    <hr>
    <div class="columns">
      <div class="columns is-3">
        <form v-on:submit.prevent="addKvp">
          <h2 class="subtitle">Add KVP</h2>
          <div class="field">
            <label class="label">Key</label>
            <div class="control">
              <input class="input" type="text" v-model="key">
            </div>
          </div>

          <div class="field">
            <label class="label">Value</label>
            <div class="control">
              <div class="control">
                <input class="input" type="text" v-model="value">
              </div>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-link">Submit</button>
            </div>
          </div>
        </form>
      </div>
      <div class="column is-3">
        <h2 class="subtitle">List of KVPs:</h2>
        <div class="kvps">
          <div class="card" v-for="kvp in kvps" v-bind:key="kvp.key">
            <div class="card-content">{{kvp.key}}: {{kvp.value}}</div>
            <footer class="card-footer">
              <a class="card-footer-item" @click="deleteKvp(kvp.id)">Delete</a>
            </footer>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      kvps: [],
      key:'',
      value:'',
    }
  },
  mounted() {
    this.getKvps()
  },
  methods: {
    getKvps() {
      axios({
        method:'get',
        url: 'https://20.39.228.116/kvp/',
        auth: {
          username:'root',
          password:'admin',
        }
      }).then(response => this.tasks = response.data)
    },
    addKvp() {
      if(this.description) {
        axios({
          method:'post',
          url: 'https://20.39.228.116/kvp/',
          data: {
            key: this.key,
            value: this.value
          },
          auth: {
            username:'root',
            password:'admin',
          }
        }).then(()=> {
          this.getKvps()
        }).catch((error)=> {
          console.log(error)
        })
      }
    },
    editKvp(kvp_id, key, value) {
      axios({
        method: 'patch',
        url: 'http://127.0.0.1:8000/kvp/' + kvp_id + '/',
        headers: {
          'Content-Type': 'application/json',
        },
        data: {
          key:key,
          value:value,
        },
        auth: {
            username:'root',
            password:'admin',
        }
      }).then(()=> {
        this.getKvps()
      }).catch((error)=> {
          console.log(error)
      })
    },
    deleteKvp(kvp_id) {
      axios({
        method: 'delete',
        url: 'http://127.0.0.1:8000/kvp/' + kvp_id + '/',
        headers: {
          'Content-Type': 'application/json',
        },
        auth: {
            username:'root',
            password:'admin',
        }
      }).then(()=> {
        this.getKvps()
      }).catch((error)=> {
          console.log(error)
      })
    }
  }
}
</script>


<style>
.select, select{
  width: 100%;
}
.card {
  margin-bottom:20px;
}
.done {
  opacity:0.3;
}
</style>