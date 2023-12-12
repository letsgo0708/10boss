<script>
    import fastapi from "../lib/api"
    import { push} from 'svelte-spa-router'
    import { onMount, afterUpdate } from "svelte"
    import List from './List.svelte'
    import List2 from './List2.svelte'
    let toggled = false

    function delete_all_cut() {
        if(window.confirm('정말로 모든 컷 기록을 삭제하시겠습니까?')) {
            let url = "/api/cut/delete_all"
            let params = {
            }
            fastapi('delete', url, params,
                (json) => {
                  toggled = !toggled // 정말 엄청난 꼼수인게 분명함
                },
                (err_json) => {
                    error = err_json
                }
            )
        }
    }

    function boss2x_update() {
        if(window.confirm('변경 이후 입력하는 컷 기록부터 적용됩니다.\n이미 입력된 컷 기록은 영향을 받지 않습니다.\n\n보스 2배 이벤트 적용/미적용 하시겠습니까?')) 
        {
            let url = "/api/option/boss2x/update"
            let params = {
            }
            fastapi('put', url, params,
                (json) => {
                  toggled = !toggled // 정말 엄청난 꼼수인게 분명함
                },
                (err_json) => {
                    error = err_json
                }
            )
        }
    }

    function reload() {
      toggled = !toggled
    }

    onMount( () => {console.log("onMount")} )
    afterUpdate( () => {console.log("afterUpdate")})

  </script>
  

  

  
  
  {#key toggled}
    <List />
  {/key}
  <div class="text-center py-2" >
    <button type="button" class="btn btn-light btn-outline-secondary btn-sm px-4 py-2 mx-1" on:click={() => delete_all_cut()}> 모든 컷 기록 삭제 </button>
    <button type="button" class="btn btn-light btn-outline-secondary btn-sm px-4 py-2 mx-1" on:click={() => reload()}> 새로고침 </button>
  </div>
    
  {#key toggled}
    <List2 />
  {/key}
  <div class="text-center pt-2 pb-4">
    <button class="btn btn-light btn-outline-secondary btn-sm px-4 py-2 mx-1" on:click={() => boss2x_update()}> 보스 2배 이벤트 적용/미적용 </button>
  </div>
  
  