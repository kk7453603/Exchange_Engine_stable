(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-3523f091"],{"0bc6":function(t,e,i){},"9eb4":function(t,e,i){"use strict";i.r(e);var s=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-container",{staticClass:"px-10"},[i("h1",[t._v(" Портфель ")]),t.portfolio.length?i("v-list",{attrs:{"two-line":"",color:"white"}},[i("v-subheader",{staticClass:"mr-8",attrs:{inset:""}},[i("span",[t._v(" Акции ")]),i("v-spacer")],1),t._l(t.portfolio,(function(e){return i("v-list-item",{key:e.title},[i("v-list-item-avatar",{attrs:{color:"grey lighten-3 text-center caption"}},[e.icon?i("v-img",{attrs:{src:e.icon}}):i("span",{staticClass:"text-center mx-auto"},[t._v(" "+t._s(e.stock)+" ")])],1),i("v-list-item-content",[i("v-list-item-title",{domProps:{textContent:t._s(e.stock)}}),e.count<0?i("v-list-item-subtitle",[t._v(" (Торговля на понижение) ")]):t._e()],1),i("v-list-item-action",[i("v-list-item-subtitle",{staticClass:"font-weight-medium mb-n2"},[t._v(" Количество: ")]),i("v-list-item-title",[t._v(" "+t._s(e.count<0?-e.count:e.count)+" ")])],1)],1)}))],2):i("h3",[t._v(" Ваш портфель пока пуст ")])],1)},n=[],a=(i("b680"),i("cb98")),o={name:"Portfolio",data:function(){return{portfolioInterval:void 0}},computed:{portfolio:function(){return this.$store.getters.portfolio}},methods:{getSecurityPrice:function(t){a["a"].get("api/v1/stocks/"+t).then((function(t){return console.log(t.data),t.data.price})).catch((function(t){console.log(t)}))},sumSecurities:function(t){var e=0;for(var i in t)e+=t[i].price;return e.toFixed(2)}}},r=o,c=i("2877"),l=i("6544"),u=i.n(l),v=i("a523"),m=i("adda"),f=i("8860"),d=i("da13"),h=i("1800"),p=i("8270"),b=i("5d23"),_=i("2fa4"),g=i("e0c7"),V=Object(c["a"])(r,s,n,!1,null,"253f368e",null);e["default"]=V.exports;u()(V,{VContainer:v["a"],VImg:m["a"],VList:f["a"],VListItem:d["a"],VListItemAction:h["a"],VListItemAvatar:p["a"],VListItemContent:b["a"],VListItemSubtitle:b["b"],VListItemTitle:b["c"],VSpacer:_["a"],VSubheader:g["a"]})},e0c7:function(t,e,i){"use strict";var s=i("5530"),n=(i("0bc6"),i("7560")),a=i("58df");e["a"]=Object(a["a"])(n["a"]).extend({name:"v-subheader",props:{inset:Boolean},render:function(t){return t("div",{staticClass:"v-subheader",class:Object(s["a"])({"v-subheader--inset":this.inset},this.themeClasses),attrs:this.$attrs,on:this.$listeners},this.$slots.default)}})}}]);
//# sourceMappingURL=chunk-3523f091.63673a93.js.map