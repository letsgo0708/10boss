<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"
  import CutDetail from './routes/CutDetail.svelte';

  const routes = {
    '/': Home,
    '/detail/:boss_id': Detail,
  }
</script>

<Router {routes}/>