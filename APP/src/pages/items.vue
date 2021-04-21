<template>
  <q-page padding>
    <li v-for="item in items" :key="item">
      {{item.nombre}}
    </li>
  </q-page>
</template>

<script>
import { Item } from 'components/models'
import item from 'components/item.vue'

export default {
  name: 'PageName',
  componets: { item },
  data () {
    return { 
      items: []
    }
  },
  methods: {
    getItems () {
      this.$api.get('/items')
        .then((res) => {
          console.log(res);
          this.items = res.data.items;
        })
        .catch(err => { console.error(err) })
    },
    updateItem() { return 0; }
  },
  mounted() {
    this.getItems();
  }
}
</script>
