<script>
    import fastapi from "../lib/api"
    import { link } from 'svelte-spa-router'
    import moment from 'moment/min/moment-with-locales'
    moment.locale('ko')
    let boss_list = []
    let boss_list_0 = [] 
    let boss_list_1 = []
    let boss_list_2 = []
    let boss_list_3 = []
    let boss2x = ""
  
    function get_boss_list() {
        fastapi('get', '/api/boss/list', {}, (json) => {
            boss_list = json
            for (let i = 0; i < boss_list.length; i++) {
              // 컷 기록이 있는 보스들만 0,1,3
              if (boss_list[i]["cuts"].length > 0 ){
                let tmp = new Object;
                // 각 보스의 가장 마지막 젠타임을 last_gen_time 으로 할당
                boss_list[i]["last_gen_time"] = boss_list[i]["cuts"].at(-1)["gen_time"]

                // 현재시각보다 30분전을 기준으로 그 이후 보스들만 목록에 표시 
                if ( new Date() - new Date(boss_list[i]["last_gen_time"]) < 1800000 ) {
                  // 현재시각 이전, 즉 1분전~30분전 보스들은 boss_list_0, 
                  if (new Date(boss_list[i]["last_gen_time"]) < new Date() ) {
                  tmp.id = boss_list[i]["id"]
                  tmp.name = boss_list[i]["name_kr"]
                  tmp.delay = boss_list[i]["delay"]
                  tmp.est_gen_time = boss_list[i]["last_gen_time"]
                  boss_list_0.push(tmp)
                  }
                  // 현재시각 이후 보스들은 boss_list_1
                  else {
                  tmp.id = boss_list[i]["id"]
                  tmp.name = boss_list[i]["name_kr"]
                  tmp.delay = boss_list[i]["delay"]
                  tmp.est_gen_time = boss_list[i]["last_gen_time"]
                  boss_list_1.push(tmp)
                  }
                  }
                else {
                  tmp.id = boss_list[i]["id"]
                  tmp.name = boss_list[i]["name_kr"]
                  tmp.delay = boss_list[i]["delay"]
                  tmp.est_gen_time = boss_list[i]["last_gen_time"]
                  boss_list_3.push(tmp)

                }
                
              // 컷 기록이 없으면 boss_list_2                
              } else {
                let tmp = new Object;
                tmp.id = boss_list[i]["id"]
                tmp.name = boss_list[i]["name_kr"]
                tmp.delay = boss_list[i]["delay"]
                boss_list_2.push(tmp)
              }

            }

            boss_list_0 = boss_list_0
            boss_list_1 = boss_list_1
            boss_list_2 = boss_list_2
            boss_list_3 = boss_list_3
            boss_list_0.sort( (a,b) => new Date(a.est_gen_time) - new Date(b.est_gen_time) ) 
            boss_list_1.sort( (a,b) => new Date(a.est_gen_time) - new Date(b.est_gen_time) ) 
            boss_list_3.sort( (a,b) => new Date(a.est_gen_time) - new Date(b.est_gen_time) ) 
            boss_list_2.sort( (a,b) => a.delay - b.delay)
            boss_list_2.sort( (a,b) => (a.name > b.name) ? 1 : -1) 
            console.log(boss_list_0) // 30분전~1분전
            console.log(boss_list_1) // 현재 시각 이후
            console.log(boss_list_2) // 컷 기록이 0회인 보스
            console.log(boss_list_3) // 멍 또는 컷 미입력 보스
            }
        ) 
    }

    function get_boss2x() {
      fastapi('get', '/api/option/boss2x', {}, (json) => {
            boss2x = json
    })}
    get_boss_list()
    get_boss2x()
  </script>

<style>

  a:link, :visited { color: black; text-decoration: none; font-weight:bold;}
  a:hover { color: rgb(75, 126, 192); text-decoration: underline; font-weight:bold;}

</style>

<section class="container">
  <div class="card p-1 m-3">
      <div class = "card-body">
        <div class = "card-title fs-5 fw-bold pb-1 text-center">
          {#if boss_list_0.length + boss_list_1.length > 0}
          텐팀 보스 스케쥴 {#if boss2x.active} : 2배 이벤트 적용중 {:else} {/if}
          {:else}
          텐팀 보스 스케쥴 없음 {#if boss2x.active} : 2배 이벤트 적용중 {:else} {/if}
          {/if}
        </div>
        <table class="table table-hover ">
          <thead class="table-success text-center">
            <tr>
              <th scope="col">보스</th>
              <th scope="col">젠 시각</th>
            </tr>
          </thead>
          <tbody class="text-center">
            {#each boss_list_0 as boss}
            <tr>
              <th scope="row"><a use:link href="/detail/{boss.id}" class="text-danger"> {boss.name} </a></th>
              <td><div class="text-danger fw-semibold">{moment(boss.est_gen_time).format("HH:mm") }</div></td>
            </tr>
            {/each}
            {#each boss_list_1 as boss}
            <tr>
              <th scope="row"><a use:link href="/detail/{boss.id}"> {boss.name} </a></th>
              <td class="fw-semibold">{moment(boss.est_gen_time).format("HH:mm")}</td>
            </tr>
            {/each}
          </tbody>
        </table>
      </div>
  </div>
</section>
