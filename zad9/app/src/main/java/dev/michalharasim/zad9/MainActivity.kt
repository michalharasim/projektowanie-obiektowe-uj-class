package dev.michalharasim.zad9

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import dev.michalharasim.zad9.models.Category
import dev.michalharasim.zad9.ui.theme.Zad9Theme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            Zad9Theme {
                App()
            }
        }
    }
}

@Composable
fun App() {
    var selectedCategory by remember { mutableStateOf<Category?>(null) }

    Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
        Box(modifier = Modifier.padding(innerPadding)) {
            if (selectedCategory == null) {
                CategoryListScreen(onCategoryClick = { category ->
                    selectedCategory = category
                })
            } else {
                CategoryDetailScreen(
                    category = selectedCategory!!,
                    onBack = { selectedCategory = null }
                )
            }
        }
    }
}

@Composable
fun CategoryListScreen(
    onCategoryClick: (Category) -> Unit,
    modifier: Modifier = Modifier
) {
    val categories = FakeData.categories

    LazyColumn(modifier = modifier.padding(16.dp)) {
        items(categories) { category ->
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .clickable { onCategoryClick(category) }
                    .padding(vertical = 14.dp)
            ) {
                Text(
                    text = category.name,
                    style = MaterialTheme.typography.bodyLarge
                )
                HorizontalDivider()
            }
        }
    }
}

@Composable
fun CategoryDetailScreen(category: Category, onBack: () -> Unit) {
    val products = FakeData.products.filter { it.categoryId == category.id }

    Column(modifier = Modifier
        .fillMaxSize()
        .padding(16.dp)) {

        Text(
            text = "Category: ${category.name}",
            style = MaterialTheme.typography.headlineMedium,
            modifier = Modifier.padding(bottom = 16.dp)
        )

        Button(
            onClick = onBack,
            modifier = Modifier.padding(bottom = 16.dp)
        ) {
            Text("Back to Category List")
        }

        LazyColumn {
            items(products) { product ->
                Column(modifier = Modifier.padding(vertical = 8.dp)) {
                    Text(
                        text = product.name,
                        style = MaterialTheme.typography.bodyLarge
                    )
                    Text(
                        text = "Price: \$${product.price}",
                        style = MaterialTheme.typography.bodyMedium
                    )
                    HorizontalDivider(modifier = Modifier.padding(top = 8.dp))
                }
            }
        }
    }
}

@Preview(showBackground = true)
@Composable
fun CategoryListPreview() {
    Zad9Theme {
        App()
    }
}
