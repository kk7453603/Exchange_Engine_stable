(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-3523f091"],{"0bc6":function(t,e,i){},"9eb4":function(t,e,i){"use strict";i.r(e);var s=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-container",{staticClass:"px-10"},[i("h1",[t._v(" Портфель ")]),t.portfolio.length?i("v-list",{attrs:{"two-line":"",color:"white"}},[i("v-subheader",{staticClass:"mr-8",attrs:{inset:""}},[i("span",[t._v(" Акции ")]),i("v-spacer")],1),t._l(t.portfolio,(function(e){return i("v-list-item",{key:e.title},[i("v-list-item-avatar",{attrs:{color:"grey lighten-3 text-center caption"}},[e.icon?i("v-img",{attrs:{src:e.icon}}):i("span",{staticClass:"text-center mx-auto"},[t._v(" "+t._s(e.stock.name)+" ")])],1),i("v-list-item-content",[i("v-list-item-title",{domProps:{textContent:t._s(e.stock.name)}}),e.count<0?i("v-list-item-subtitle",[t._v(" (Торговля на понижение) ")]):t._e()],1),e.count<0?i("v-list-item-action",[i("v-list-item-title",{staticClass:"font-weight-medium mb-n2"},[t._v(" "+t._s(e.count)+" x "+t._s((-e.count*e.stock.price).toFixed(2))+"₮ ")]),i("v-list-item-title",{class:e.stock.price-e.aver_price<0?"green--text":e.stock.price-e.aver_price>0?"red--text":"grey--text"},[t._v(" "+t._s((e.count*(e.stock.price-e.aver_price)).toFixed(2))+"₮ "),i("span",{staticClass:"grey--text"},[t._v(" | ")]),t._v(" "+t._s(((e.stock.price-e.aver_price)/e.stock.price*-100).toFixed(2))+"% ")])],1):i("v-list-item-action",[i("v-list-item-title",{staticClass:"font-weight-medium mb-n2"},[t._v(" "+t._s(e.count)+" x "+t._s(e.stock.price.toFixed(2))+"₮ ")]),i("v-list-item-title",{class:e.stock.price-e.aver_price<0?"red--text":e.stock.price-e.aver_price>0?"green--text":"grey--text"},[t._v(" "+t._s((e.count*(e.stock.price-e.aver_price)).toFixed(2))+"₮ "),i("span",{staticClass:"grey--text"},[t._v(" | ")]),t._v(" "+t._s(((e.stock.price-e.aver_price)/e.stock.price*100).toFixed(2))+"% ")])],1)],1)}))],2):i("h3",[t._v(" Ваш портфель пока пуст ")])],1)},o=[],c=(i("b680"),i("cb98")),r={name:"Portfolio",data:function(){return{portfolioInterval:void 0}},computed:{portfolio:function(){return console.log(this.$store.getters.portfolio),this.$store.getters.portfolio}},methods:{getSecurityPrice:function(t){c["a"].get("api/v1/stocks/"+t).then((function(t){return console.log(t.data),t.data.price})).catch((function(t){console.log(t)}))},sumSecurities:function(t){var e=0;for(var i in t)e+=t[i].price;return e.toFixed(2)}}},a=r,n=i("2877"),l=i("6544"),v=i.n(l),u=i("a523"),p=i("adda"),m=i("8860"),d=i("da13"),_=i("1800"),f=i("8270"),h=i("5d23"),x=i("2fa4"),b=i("e0c7"),g=Object(n["a"])(a,s,o,!1,null,"442e0d13",null);e["default"]=g.exports;v()(g,{VContainer:u["a"],VImg:p["a"],VList:m["a"],VListItem:d["a"],VListItemAction:_["a"],VListItemAvatar:f["a"],VListItemContent:h["a"],VListItemSubtitle:h["b"],VListItemTitle:h["c"],VSpacer:x["a"],VSubheader:b["a"]})},e0c7:function(t,e,i){"use strict";var s=i("5530"),o=(i("0bc6"),i("7560")),c=i("58df");e["a"]=Object(c["a"])(o["a"]).extend({name:"v-subheader",props:{inset:Boolean},render:function(t){return t("div",{staticClass:"v-subheader",class:Object(s["a"])({"v-subheader--inset":this.inset},this.themeClasses),attrs:this.$attrs,on:this.$listeners},this.$slots.default)}})}}]);
//# sourceMappingURL=chunk-3523f091.dbdf5543.js.map