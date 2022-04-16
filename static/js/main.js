let cashLstTable

function update(oldData, newData) {
    if (oldData === undefined) {
        cashLstTable = newData
        return newData
    }
    return oldData
}

function createCell(text, tr){
    let td = document.createElement('td')
    td.innerHTML = text
    tr.appendChild(td)
}

function createPageTable(pageNum, notesOnePage, alldataUnnamed, table){


    let start = (pageNum - 1)  * notesOnePage
    let end = start + notesOnePage

    let notes = alldataUnnamed.slice(start, end)
    cash__field = table.rows[0].innerHTML
    table.innerHTML= ''

    let tr = document.createElement('tr')
    tr.innerHTML = cash__field
    table.appendChild(tr)


    for (let note of notes){
        let tr = document.createElement('tr')
        table.appendChild(tr)
        createCell(note.id, tr)
        createCell(note.date, tr)
        createCell(note.name, tr)
        createCell(note.amount, tr)
        createCell(note.distanse, tr)
        }
}

// ---------------- Пагинация------------------
function createPagenation(alldataUnnamed) {
    alldataUnnamed = update(cashLstTable, alldataUnnamed)
    let table = document.querySelector('#myTablePage')
    let pagination = document.querySelector('#id_pagination')

    let notesOnePage = 4

    let countOfItems = Math.ceil(alldataUnnamed.length / notesOnePage)

    // Создаем страницы
    let items = []
    for (let i = 1; i <= countOfItems; i++){
        let li = document.createElement('li')
        li.innerHTML = i
        pagination.appendChild(li)
        items.push(li)
    }

    // Дефолтная таблица
    createPageTable(1, notesOnePage, alldataUnnamed, table)

    // Таблица по странице
    for (let item of items){
        item.addEventListener('click', function(){
            let pageNum = +this.innerHTML
            createPageTable(pageNum, notesOnePage, alldataUnnamed, table)
            })
        }
    }


// ---------------- Поиск по имени отдельно (Доп)  ------------------
function tableSearch(alldataUnnamed) {
    alldataUnnamed = update(cashLstTable, alldataUnnamed)

    cash = []
    var phrase = document.getElementById('search-name2');
    var regPhrase = new RegExp(phrase.value, 'i');
    var flag = false;
    for (var i = 0; i < alldataUnnamed.length; i++) {

        if (regPhrase.test(alldataUnnamed[i].name)){
        cash.push(alldataUnnamed[i])
        }
    createPageTable(1, 4, cash, document.querySelector('#myTablePage'))
    }
}

// ---------------- Поиск по выбранным полям #------------------
function searchForParametr2(alldataUnnamed){
alldataUnnamed = update(cashLstTable, alldataUnnamed)

cash = []
let indexField=document.getElementById('caseField').value;
let caseIF=document.getElementById('caseIF').value;
let filter=document.getElementById('filter').value;

    //Критерий поиска
    var phrase = document.getElementById('filter').value;


    var table = document.getElementById('myTable');

    var regPhrase = new RegExp(phrase.value, 'i');

    var flag = false;
    for (var i = 0; i < alldataUnnamed.length; i++) {

        flag = false;
        current_data = alldataUnnamed[i][indexField]
        if (caseIF == '>'){
                            if (current_data > phrase) {
                                    flag = true
                                }
                            }
        else if (caseIF == '='){
                             if (parseInt(current_data) === parseInt(phrase)) {
                                    flag = true
                                }
                            }
        else if (caseIF == '<'){
                            if (current_data < phrase) {
                                    flag = true
                                }
                            }
        else
        {
         flag = current_data.includes(phrase)
        }
        if (flag) {
            cash.push(alldataUnnamed[i])
        }
    }
    createPageTable(1, 4, cash, document.querySelector('#myTablePage'))
}

function byField(field) {
  return (a, b) => a[field] > b[field] ? 1 : -1;
}
// ---------------- Сортировка таблицы по полям ------------------
function sortTable(indexField, alldataUnnamed) {
    alldataUnnamed = update(cashLstTable, alldataUnnamed)

    if (indexField ===0) {
        nameField = 'id'
    }
    else if (indexField ===2) {
        nameField = 'name'
    }
    else if (indexField === 3) {
        nameField = 'amount'
    }
    else {
        nameField = 'distanse'
    }
    flag_sort = true

    alldataUnnamed.sort(byField(nameField));

    createPageTable(1, 4, alldataUnnamed, document.querySelector('#myTablePage'))
}