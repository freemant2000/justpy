// var c1=new Vue({el:"#a123",template:
// `<quasar_component 
// :jp_props="{html_tag:'q-btn',
// vue_type:'quasar_component',
// attrs:{label:'Hi'},
// object_props:[],
// events:[],
// scoped_slots:{
//     default:{
//         vue_type:'html_component',
//         html_tag:'b',
//         object_props:[],
//         events:[],
//         text:'Hi'}}}"></quasar_component>`})

    // var scoped_slots = {};
    // var b = {};
    // for (e in this.jp_props.scoped_slots) {
    //     let slot_name = e;
    //     b[slot_name] = this.jp_props.scoped_slots[slot_name];
    //     let vue_type = b[slot_name].vue_type;
    //     scoped_slots[slot_name] = function () {
    //             return h(vue_type, {props: {jp_props: b[slot_name]}});}}

    // scoped_slots["loading"] = function () {
    //     return h("b", 3)
    // }        
    // description_object['scopedSlots'] = scoped_slots;

    // return h(this.jp_props.html_tag, description_object, comps);

var myapp=new Vue({
    el: "#a123",
    data: {n:{html_tag: 'q-tree', 
    attrs: {nodes:[{n:'pen',p:4}],
    nodeKey:"n", labelKey:"p"}, 
    scoped_slots: {"default-header":{js_body:"h('b',ps.node.n)"}}, 
    object_props: [],
    events: []}}, 
    template: `<quasar_component
                    :jp_props="n">
                </quasar_component>`});